from app import app
from flask import render_template, request, Response, jsonify
from app.discord import sendDetailsToDiscord
from flask_restful import Resource, Api
import sys
api = Api(app)

@app.route('/',methods=["GET"])
@app.route('/',methods=["GET"])
def index():
    return render_template("/www/index.html")

@app.route('/submitted',methods=["GET", "POST"])
def submitted():
    if request.method == 'POST':
        sendDetailsToDiscord(request.form['name'],request.form['email'],request.form['phone'],request.form['state'],request.form['course'],request.environ['REMOTE_ADDR'],request.headers.get('User-Agent')) #need to ad request ip and request web client
        
    if Response.status_code == 400:
        return render_template("/www/error.html",error = 400)

    return render_template("/www/submitted.html")

class Form(Resource):
    def get(self):
        return {
            'Form': {
                'name': 'Please input your last name',
                'email': 'Please input your email',
                'phone': 'Please input your phone',
                'state' : 'please input your state',
                'course' : 'The courses available differ per state, please refer to the table below'
        },

        'State Courses' :
        {
            'act': 'Specialist, Methods, Applications, Essential, Year10, Year9, Year8, Year7, other',
            'nsw' : 'Extension, Advanced, Standard, Year10, Year9, Year8, Year7, other',
            'nt': 'N/A',
            'qld':'N/A',
            'sa' : 'N/A',
            'tas' : 'General, Methods, Specialised, Preliminary, Year10, Year9, Year8, Year7, other',
            'vic': 'Specialist, Methods, General, Further Maths, Foundations, Year10, Year9, Year8, Year7, other',
            'wa' : 'Specialist, Methods, Applications, Essential, Foundations, OLNA, Year10, Year9, Year8, Year7, other',
            'other': 'N/A'
        }


        }

    def post(self):     
        this = request.json
        print(this)
        sendDetailsToDiscord(request.json['name'],request.json['email'],request.json['phone'],request.json['state'],request.json['course'],request.environ['REMOTE_ADDR'],request.headers.get('User-Agent')) #need to ad request ip and request web client
        return {
            "message":"Your request has been successful, a tutor will contact you shortly."
        }


api.add_resource(Form, '/api')