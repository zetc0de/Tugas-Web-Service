from customers import *
from ekyc import *
from werkzeug.utils import secure_filename
import datetime



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
        resp = Response('{"msg":"Data not found"}', status=404, mimetype='application/json')
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
        resp = Response('{"msg":"All field must be completed"}', status=422, mimetype='application/json')
        return resp
    else:
        CompanyName = req_data["CompanyName"]
        ContactName = req_data["ContactName"]
        ContactTitle = req_data["ContactTitle"]
        Address = req_data["Address"]
        City = req_data["City"]
        # KTP_url = req_data["KTP_url"]
        Customers.add_customer(CompanyName,ContactName,ContactTitle,Address,City)
        resp = Response('{"msg":"Customer created"}', status=201, mimetype='application/json')
        return resp

#update customer by id
@app.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    req_data = request.get_json()
    if req_data is None:
        resp = Response('{"msg":"All field must be completed"}', status=422, mimetype='application/json')
        return resp
    else:
        CompanyName = req_data["CompanyName"]
        ContactName = req_data["ContactName"]
        ContactTitle = req_data["ContactTitle"]
        Address = req_data["Address"]
        City = req_data["City"]
        # KTP_url = req_data["KTP_url"]
        update = Customers.update_customer(id,CompanyName,ContactName,ContactTitle,Address,City)
        if update == True:
            resp = Response('{"msg":"Customer updated"}', status=200, mimetype='application/json')
            return resp
        else:
            resp = Response('{"msg":"Data not found"}', status=404, mimetype='application/json')
            return resp   

#delete customer by id
@app.route('/customers/<int:id>', methods=['DELETE'])
def del_customer(id):
    delete = Customers.del_customer(id)
    if delete == True:
        resp = Response('{"msg":"Customer deleted"}', status=200, mimetype='application/json')
        return resp
    else:
        resp = Response('{"msg":"Data not found"}', status=404, mimetype='application/json')
        return resp


#allowed extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#upload ekyc
@app.route('/ekyc/<int:id>', methods=['POST'])
def upload_ekyc(id):
    # ktp = request.files['fileKTP']
    # selfie = request.files['fileSelfie']
    # time_now  = datetime.datetime.now().strftime('%m_%d_%Y_%H%M%S') 
    # if ktp.filename == '':
    #     flash('No selected file')
    # elif ktp and allowed_file(ktp.filename) :
    #     ktp_filename = secure_filename(time_now  + "_" + str(id) + "_" + ktp.filename)
    #     ktp.save(os.path.join(app.config['UPLOAD_FOLDER']['ktp'],ktp_filename))
    
    # if selfie.filename == '':
    #     flash('No selected file')
    # elif selfie and allowed_file(selfie.filename) :
    #     selfie_filename = secure_filename(time_now + "_" + str(id) + "_" + selfie.filename)
    #     selfie.save(os.path.join(app.config['UPLOAD_FOLDER']['selfie'],selfie_filename))


    # upload = Ekyc.upload_ekyc(id,ktp_filename,selfie_filename)
    # if upload == True:
    #     resp = Response("Upload successfully", status=200, mimetype='application/json')
    #     return resp
    # else:
    #     resp = Response("Upload Failed", status=422, mimetype='application/json')
    #     return resp
    #11_11_2021_153903_1_logo.png
    ktp = request.files['fileKTP']
    selfie = request.files['fileSelfie']
    time_now  = datetime.datetime.now().strftime('%m_%d_%Y_%H%M%S') 
    ekyc = Ekyc.query.filter_by(customer_id=id).first()   
    isNone, data = Customers.get_customer(id)
    if isNone == False:
        resp = Response('{"msg":"Data not found"}', status=404, mimetype='application/json')
        return resp
    elif ekyc is not None:
        resp = Response('{"msg":"eKYC already filled, use PUT method please"}', status=422, mimetype='application/json')
        return resp
    elif ktp.filename == '' or selfie.filename == '':
        resp = Response('{"msg":"All field must be filled"}', status=422, mimetype='application/json')
        return resp
    elif ktp and selfie and allowed_file(ktp.filename) and allowed_file(selfie.filename):
        #ktp
        ktp_filename = secure_filename(time_now  + "_" + str(id) + "_" + ktp.filename)
        ktp.save(os.path.join(app.config['UPLOAD_FOLDER']['ktp'],ktp_filename))
        print(ktp.save)
        #selfie
        selfie_filename = secure_filename(time_now + "_" + str(id) + "_" + selfie.filename)
        selfie.save(os.path.join(app.config['UPLOAD_FOLDER']['selfie'],selfie_filename))

        #update ke db    
        Ekyc.upload_ekyc(id,ktp_filename,selfie_filename)
        resp = Response('{"msg":"Upload successfully"}', status=201, mimetype='application/json')
        return resp
        # return Response(ktp_filename, status=201, mimetype='application/json')
    else:    
        resp = Response('{"msg":"Allowed file type : .png, .jpg, .jpeg"}', status=422, mimetype='application/json')
        return resp  


#update ekyc
@app.route('/ekyc/<int:id>',methods=['PUT'])
def update_ekyc(id):
    ktp = request.files['fileKTP']
    selfie = request.files['fileSelfie']
    time_now  = datetime.datetime.now().strftime('%m_%d_%Y_%H%M%S') 
    # ekyc = Ekyc.query.filter_by(customer_id=id).first() 
    isNone, data = Customers.get_customer(id)  
    if isNone == False:
        resp = Response('{"msg":"Data not found"}', status=404, mimetype='application/json')
        return resp
    elif ktp.filename == '' or selfie.filename == '':
        resp = Response('{"msg":"All field must be filled"}', status=422, mimetype='application/json')
        return resp
    elif ktp and selfie and allowed_file(ktp.filename) and allowed_file(selfie.filename):
        #save ktp
        ktp_filename = secure_filename(time_now  + "_" + str(id) + "_" + ktp.filename)
        ktp.save(os.path.join(app.config['UPLOAD_FOLDER']['ktp'],ktp_filename))
        print(ktp.save)
        #save selfie
        selfie_filename = secure_filename(time_now + "_" + str(id) + "_" + selfie.filename)
        selfie.save(os.path.join(app.config['UPLOAD_FOLDER']['selfie'],selfie_filename))

        #update ke db    
        Ekyc.update_ekyc(id,ktp_filename,selfie_filename)
        resp = Response('{"msg":"Update successfully"}', status=201, mimetype='application/json')
        return resp
        # return Response(ktp_filename, status=201, mimetype='application/json')
    else:    
        resp = Response('{"msg":"Allowed File Type : .png, .jpg, .jpeg"}', status=422, mimetype='application/json')
        return resp   


    #hapus file lama
    # ekyc = Ekyc.get_ekyc(id)

    # if 'Not uploaded yet' in ekyc:
    #         resp = Response("Data not found", status=404, mimetype='application/json')
    #         return resp
    # else:
    #     old_ktp = ekyc[0]['ktp_filename']
    #     old_selfie = ekyc[0]['selfie_filename']
    #     os.remove(old_ktp)
    #     os.remove(old_selfie)
    #hapus file lama
    # ekyc = Ekyc.del_ekyc(id)


if __name__ == "__main__":
    app.run(port=1234, debug=True)