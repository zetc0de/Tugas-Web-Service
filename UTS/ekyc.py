import os
from settings import *
import json
from customers import *

class Ekyc(db.Model):
    __tablename__ = "ekyc"
    id = db.Column(db.Integer, primary_key=True)
    ktp_filename = db.Column(db.String(100), nullable=False)
    selfie_filename = db.Column(db.String(100), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.CustomerID'))

    def json(self):
        return {
            "ekycID":self.id,
            "ktp_filename":self.ktp_filename,
            "selfie_filename":self.selfie_filename
        }
    
    def upload_ekyc(id,ktp_filename,selfie_filename):
        ktp_filename = app.config["UPLOAD_FOLDER"]["ktp"] + ktp_filename
        selfie_filename = app.config["UPLOAD_FOLDER"]["selfie"] + selfie_filename
        newEkyc = Ekyc(customer_id=id,ktp_filename=ktp_filename,selfie_filename=selfie_filename)
        db.session.add(newEkyc)
        db.session.commit()

    def update_ekyc(id,ktp_filename,selfie_filename):
        # del_ekyc = Ekyc.del_ekyc(id)
        # print("Delete ekyc :" + str(del_ekyc))
        ktp_filename = app.config["UPLOAD_FOLDER"]["ktp"] + ktp_filename
        selfie_filename = app.config["UPLOAD_FOLDER"]["selfie"] + selfie_filename
        ekyc = Ekyc.query.filter_by(customer_id=id).first()   
        ekyc.ktp_filename = ktp_filename
        ekyc.selfie_filename = selfie_filename
        db.session.commit()  


    def get_ekyc(id):
        ekyc = Ekyc.query.filter_by(customer_id=id).first()
        if ekyc is None:
            ekyc = 'Not uploaded yet'
        else:
            ekyc = [Ekyc.json(ekyc)]
        return ekyc

    def del_ekyc(id):
        ekyc = Ekyc.query.filter_by(customer_id=id).first()
        ekycID = Ekyc.json(ekyc)['ekycID']
        old_ktp = Ekyc.json(ekyc)['ktp_filename']
        old_selfie = Ekyc.json(ekyc)['selfie_filename']
        del_ekyc = Ekyc.query.filter_by(id=ekycID).delete()
        if del_ekyc == False:
            return False
        else:
            print(old_ktp + " will be removed!")
            os.remove(old_ktp)
            os.remove(old_selfie)
            return True
            