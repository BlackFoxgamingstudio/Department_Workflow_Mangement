from flask import Flask
from flask import request
from flask import Flask, jsonify
from flask import abort
import os
from flask import Flask, render_template, url_for, json, request, flash, redirect
import json
import requests
from werkzeug import secure_filename
import os
import pickle
import sys
import csv
import time
import sys
import datetime


from flask import make_response, flash
from flask import session as login_session

from flask import abort
from flask import make_response
from flask import request
from flask import url_for

import os
# add mongo db alta


import pprint

from werkzeug.routing import BaseConverter, ValidationError
from itsdangerous import base64_encode, base64_decode


import urllib, json

import httplib2
import json
import requests
import random
import string
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, IntegerField, TextAreaField, validators, StringField, SubmitField
 
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

#app.config['MONGO_DBNAME'] = 'keytechlabs'
#app.config['MONGO_URL'] = 'mongodb://naruto45me:N%40ruto45me@ds062448.mlab.com:62448/keytechlabs'
#mongo = PyMongo(app)




# testing notification function   
@app.route('/test')
def index():
    return render_template('test.html')


@app.route("/cal1", methods=['GET', 'POST'])
def Concole_cal1():
    counter = 0
    arry = []
    error = None
    rows = zip(arry)
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
            flash('Invalid credentials')
            with open('wincsv5.csv') as csvfile:
                reader = csv.DictReader(csvfile)
        for row in reader:
            if new_name in row['CaseOwner']:
                    if row['License'] =='':
                        output = row['License'], row['Subject'], row['id']
                        ## by calling output we now can control the output into what is place in to arry and, down the line what is writen in to the csv
                        arry.append(str(output))
                        flash(output)
                        counter = counter+1
                        flash("count of all cases with the keyword:",'red'), colored(new_name, 'green'), colored(counter,'red')
        ##I learned how to use zip()! it helps package the array to be unpackage later by the for loop##
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('microtest3.html', error=error)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
            return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

#update a usecase
# @app.route('/Community/<int:community_id>/edit/', methods = ['GET','POST'])
# def editCommunity(community_id):
#   editedCommunity = session.query(Community).filter_by(id = community_id).one()
#   if request.method == 'POST':
#       if request.form['name']:
#         editedCommunity.name = request.form['name']
#       if request.form['info']:
#         editedCommunity.info = request.form['info']
#       if request.form['zipcode1']:
#         editedCommunity.zipcode1 = request.form['zipcode1']
#       if request.form['zipcode2']:
#         editedCommunity.zipcode2 = request.form['zipcode2']
#       if request.form['zipcode3']:
#         editedCommunity.zipcode3 = request.form['zipcode3']
#         session.add(editedCommunity)
#         session.commit() 
#         flash('Community Successfully Edited %s' % editedCommunity.name)
#         return redirect(url_for('showCommunity'))
#   else:
#     return render_template('Community_edit.html', community = editedCommunity)



@app.route('/support/diagrams/<int:data_ID>/', methods=['GET'])
def showdiagram(data_ID):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "diagrams.json")
    json_url2 = os.path.join(SITE_ROOT, "static/data", "columns2.json")
    dig = json.load(open(json_url))
    num  =int(data_ID)-2
    num2 = jsonify({'data': data[num]})
    num3 = data[num]
    columns2 =json.load(open(json_url2))

    return render_template('diagram_lexy.html', dig=dig, num=num, num2=num2,num3=num3, columns2=columns2)

@app.route('/support/diagrams')
def showdiagrams():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "diagrams.json")
    dig = json.load(open(json_url))
    return render_template('codec.html', dig=dig)
# Profile per Id
class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    ID = IntegerField('ID:')
    topic = TextField('topic:', validators=[validators.required()])
    deviceversion = TextField('deviceversion:')
    issue = TextField('issue:')
    solution = TextField('solution:')
    trigger = TextField('trigger:')
    alternatieflow = TextField('alternatieflow:')
    documentation = TextField('documentation:')
    workflow = TextField('workflow:')
    definiation = TextField('definiation:')
    def reset(self):
        blankData = MultiDict([ ('csrf', self.reset_csrf() ) ])
        self.process(blankData)

@app.route('/support/api/v1.0/usecase/profile/<int:data_ID>/', methods=['GET','POST'])
def get_data(data_ID):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "usecase.json")
    json_url2 = os.path.join(SITE_ROOT, "static/data", "columns.json")
    json_url3 = os.path.join(SITE_ROOT, "static/data", "diagrams.json")
  
    data = json.load(open(json_url))
    datas = json.load(open(json_url))
    num = int(data_ID)-1
    num2 = jsonify({'data': data[num]})
    num3 = data[num]
    columns =json.load(open(json_url2))
    dig=json.load(open(json_url3))
    all_cases_counter = 0
    Number_of_worflow = 0
    # endpoint to update data from FORM
    # form post
    form = ReusableForm(request.form)
    

    if request.method == 'POST':
        name=request.form['name']
        ID= int(request.form['ID']) 
        topic=request.form['topic']

        with open('static/data/usecase.json', "r+") as jsonfile:
            update = json.load(jsonfile)
            row = ID - 1
           

            tmp = update[row]["SUBJECT"]
            update[row]["SUBJECT"] = name
            jsonfile.seek(0)  # rewind
            tmp2 = update[row]["ID"]
            update[row]['ID'] = ID
            jsonfile.seek(0)  # rewind
            tmp3 = update[row]["TOPIC"]
            update[row]["TOPIC"] = topic

            jsonfile.seek(0)  # rewind
            json.dump(update, jsonfile)
            jsonfile.truncate()

        if form.validate():
            # Save the comment here.
            flash('Hello ' + name)
        else:
            flash('Error: All the form fields are required. ')
    #end of update endpoint
    
    with open('static/data/wincsv5.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            all_cases_counter = all_cases_counter+1
    #with open('/static/data/usecase.json', 'w') as data_file:
     #   json.dump(request.form, data_file)

    return render_template('nav.html',reader=reader,datas=datas, data=data, num=num, num2=num2,num3=num3, columns=columns, dig=dig, all_cases_counter=all_cases_counter, Number_of_worflow=Number_of_worflow, form=form)


@app.route('/support/usecases')
def showjson():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "usecase.json")
    json_url2 = os.path.join(SITE_ROOT, "static/data", "columns.json")
    # csv to Json

    # json join to json
    #dictA = json.loads(json_url)
   # dictB = json.loads(json_url2)
    #merged_dict = {key: value for (key, value) in (dictA.items() + dictB.items())}
    # string dump of the merged dict
    #jsonString_merged = json.dumps(merged_dict)    
    #add to data
    data = json.load(open(json_url))
    columns =json.load(open(json_url2))
    




    return render_template('results.html', data=data, columns = columns)



@app.route('/support/api/v1.0/usecase', methods=['GET'])
def get_usecases():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT, "static/data", "usecase.json")
	data = json.load(open(json_url))
	return jsonify({'data': data})
#read api per ID
@app.route('/support/api/v1.0/usecase/<int:data_ID>', methods=['GET'])
def get_usecase(data_ID):
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT, "static/data", "usecase.json")
	data = json.load(open(json_url))
	num  =int(data_ID)-1
	return jsonify({'data': data[num]})

# @app.route('/support/api/v1.0/usecase/profile/<int:data_ID>/', methods=['GET'])
# def get_usecaseprofile(data_ID):
# 	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
# 	json_url = os.path.join(SITE_ROOT, "static/data", "usecase.json")
# 	json_url2 = os.path.join(SITE_ROOT, "static/data", "columns.json")
# 	data = json.load(open(json_url))
# 	num  =int(data_ID)-1
# 	columns =json.load(open(json_url2))
# 	return render_template()

@app.route('/api')
def hello_world():
    return 'Hello, World!'

#@app.route('/api/devices' methods=['GET', 'POST'])
#def devices():

#tasks = [
#    {
#        'id': 1,
#        'title': u'Buy groceries',
#        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
#        'done': False
#    },
#    {
#        'id': 2,
#        'title': u'Learn Python',
#        'description': u'Need to find a good Python tutorial on the web', 
#        'done': False
#    }
#]

devices = [
	{
		'id':1,
		'title': u'EDA',
		'description': u'our discovry application that captures wire data',
		'done': False
	},
	{
		'id':2,
		'title': u'EXA',
		'description': u'our records application that captures records from devices',
		'done': False
	}

]
@app.route('/support/api/v1.0/devices', methods=['POST'])
def create_device():
    if not request.json or not 'title' in request.json:
        abort(400)
    device = {
        'id': devices[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    devices.append(device)
    return jsonify({'device': device}), 201

@app.route('/support/api/v1.0/devices<int:device_id>', methods=['GET'])
def get_device(device_id):
    device = [device for device in devices if device['id'] == device_id]
    if len(device) == 0:
        abort(404)
    return jsonify({'device': device[0]})

@app.route('/support/api/v1.0/devices', methods=['GET'])
def get_devices():
	return jsonify({'devices': devices})
#@app.route('/todo/api/v1.0/tasks', methods=['GET'])
#def get_tasks():
    #return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)
