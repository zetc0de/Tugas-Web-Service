from os import pipe
from settings import *
import json
from ekyc import *

class Customers(db.Model):
    __tablename__ = 'customers'
    CustomerID = db.Column(db.Integer, primary_key=True)
    CompanyName = db.Column(db.String(50), nullable=False)
    ContactName = db.Column(db.String(50), nullable=False)
    ContactTitle  = db.Column(db.String(50), nullable=False)
    Address  = db.Column(db.String(50), nullable=False)
    City  = db.Column(db.String(50), nullable=False)
    # KTP_url = db.Column(db.String(100), nullable=False)
    ekyc = db.relationship('Ekyc', backref='author', lazy='dynamic')

    def json(self):
        return {
            'CustomerID':self.CustomerID,
            'CompanyName':self.CompanyName,
            'ContactName':self.ContactName,
            'ContactTitle':self.ContactTitle,
            'Address':self.Address,
            'City':self.City,
            "ekyc":Ekyc.get_ekyc(self.CustomerID)
            }
            # 'City':self.City,
            # 'KTP_url':self.KTP_url }
    
    def add_customer(CompanyName,ContactName,ContactTitle,Address,City):
        newCustomer = Customers(CompanyName=CompanyName,ContactName=ContactName,ContactTitle=ContactTitle,Address=Address,City=City)
        db.session.add(newCustomer)
        db.session.commit()
    
    def get_all_customer():
        # ekyc = Ekyc.get_ekyc
        return [Customers.json(customer) for customer in Customers.query.all()]
    
    def get_customer(id):
        customer = Customers.query.filter_by(CustomerID=id).first()
        if customer is None:
            return False, False
        else:
            customer = [Customers.json(customer)]
            return True, customer

    def update_customer(CustomerID,CompanyName,ContactName,ContactTitle,Address,City):
        customer_update = Customers.query.filter_by(CustomerID=CustomerID).first()
        if customer_update is None:
            return False
        else:
            customer_update.CompanyName = CompanyName
            customer_update.ContactName = ContactName
            customer_update.ContactTitle = ContactTitle
            customer_update.Address = Address
            customer_update.City = City
            # customer_update.KTP_url = KTP_url
            db.session.commit()  
            return True

    def del_customer(id):
        customer_delete = Customers.query.filter_by(CustomerID=id).delete()
        # customer = Customers.query.filter_by(CustomerID=id).first()
        # ekyc_del = Ekyc.query.filter_by(customer_id=id).delete()
        
        if customer_delete == False:
            return False
        # if customer is None:
        #     print("non?")
        #     return False
        else:
            print("asdasd")
            Ekyc.del_ekyc(id)
            db.session.commit()
            return True

    
