from customers import *

#get all customer data
@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify({'Data' : 
        {'Customers': Customers.get_all_customer()}
    })

#get customer by id
@app.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    isNone, data = Customers.get_customer(id)
    # print("Data : ", data)
    if isNone == False:
        resp = Response("Data Not Found", status=404, mimetype='application/json')
        return resp
    else:
        return jsonify({'Data': data}
    )

# add customer
@app.route('/customers', methods=['POST'])
def add_customer():
    # print(req_data)
    req_data = request.get_json()
    if req_data is None:
        resp = Response("All field must be completed", status=422, mimetype='application/json')
        return resp
    else:
        CompanyName = req_data["CompanyName"]
        ContactName = req_data["ContactName"]
        ContactTitle = req_data["ContactTitle"]
        Address = req_data["Address"]
        City = req_data["City"]
        KTP_url = req_data["KTP_url"]
        Customers.add_customer(CompanyName,ContactName,ContactTitle,Address,City,KTP_url)
        resp = Response("Customer added", status=201, mimetype='application/json')
        return resp

#update customer by id
@app.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    req_data = request.get_json()
    if req_data is None:
        resp = Response("All field must be completed", status=422, mimetype='application/json')
        return resp
    else:
        CompanyName = req_data["CompanyName"]
        ContactName = req_data["ContactName"]
        ContactTitle = req_data["ContactTitle"]
        Address = req_data["Address"]
        City = req_data["City"]
        KTP_url = req_data["KTP_url"]
        Customers.update_customer(id,CompanyName,ContactName,ContactTitle,Address,City,KTP_url)
        resp = Response("Customer updated", status=200, mimetype='application/json')
        return resp

#delete customer by id
@app.route('/customers/<int:id>', methods=['DELETE'])
def del_customer(id):
    Customers.del_customer(id)
    resp = Response("Customer deleted", status=200, mimetype='application/json')
    return resp

if __name__ == "__main__":
    app.run(port=1234, debug=True)