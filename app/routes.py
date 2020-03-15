from app import app
from flask import render_template, request, Response
from app.discord import sendDetailsToDiscord
from flask_restful import Resource, Api
import sys
api = Api(app)

@app.route('/www',methods=["GET"])
@app.route('/www',methods=["GET"])
def index():
    return render_template("/www/index.html")

@app.route('/www/submitted',methods=["GET", "POST"])
def submitted():
    if request.method == 'POST':
        print("TEST")
        name = "Dean"
        email = "dean.vains@outlook.com"
        phone = "0428802464"
        state = "wa"
        course = "applications"
        sendDetailsToDiscord(request.form['name'],request.form['email'],request.form['phone'],request.form['state'],request.form['course'],request.environ['REMOTE_ADDR'],request.headers.get('User-Agent')) #need to ad request ip and request web client
        
    if Response.status_code == 400:
        return render_template("/www/error.html",error = 400)

    return render_template("/www/submitted.html")

class Form(Resource):
    def get(self):
        return {
            'Form': {
                'firstname': 'Please input your first name',
                'lastname': 'Please input your last name',
                'email': 'Please input your email',
                'phone': 'Please input your phone',
        }
        }


api.add_resource(Form, '/')