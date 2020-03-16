from app import app

import sys
import logging
import os

import requests
import yagmail

from flask import render_template, request, Response, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS


app = Flask(__name__)


def sendDetailsToEmail(name, email, phone, state, course, address, browser):

    message = createMessage(name, email, phone, state, course, address, browser)

    yag = yagmail.SMTP('russell.error.reporting@gmail.com')
    contents = [message]
    yag.send('lachie.russell@gmail.com', 'New Client', contents)


def createMessage(name, email, phone, state, course, address, browser):
    str = f"""
        Hello Tutors, \n My name is {name} and I would like to apply for tutoring in {course}.
        State: {state}
        My email address is: {email}
        My phone number is: {phone}
        
        Browser: {browser}
        IP:      {address}
    """
    return str


api = Api(app)
CORS(app)
GA_TRACKING_ID = os.environ.get("GA_TRACKING_ID")


def track_event(category, action, label=None, value=0):
    data = {
        'v': '1',  # API Version.
        'tid': GA_TRACKING_ID,  # Tracking ID / Property ID.
        # Anonymous Client Identifier. Ideally, this should be a UUID that
        # is associated with particular user, device, or browser instance.
        'cid': '555',
        't': 'event',  # Event hit type.
        'ec': category,  # Event category.
        'ea': action,  # Event action.
        'el': label,  # Event label.
        'ev': value,  # Event value, must be an integer
        'ua': 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14'
    }
    response = requests.post(
        'https://www.google-analytics.com/collect', data=data
    )

    # If the request fails, this will raise a RequestException. Depending
    # on your application's needs, this may be a non-error and can be caught
    # by the caller.
    response.raise_for_status()


@app.route('/',methods=["GET"])
def index():
    track_event(
        category='Example',
        action='test action')
    return render_template("/www/index.html")


@app.route('/submitted',methods=["GET", "POST"])
def submitted():
    track_event(
        category='Example',
        action='test action')
    if request.method == 'POST':
        sendDetailsToEmail(
            request.form['name'],
            request.form['email'],
            request.form['phone'],
            request.form['state'],
            request.form['course'],
            request.environ['REMOTE_ADDR'],
            request.headers.get('User-Agent')
        ) #need to ad request ip and request web client
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
        'State Courses' : {
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
        sendDetailsToEmail(
            request.json['name'],
            request.json['email'],
            request.json['phone'],
            request.json['state'],
            request.json['course'],
            request.environ['REMOTE_ADDR'],
            request.headers.get('User-Agent')
        ) #need to ad request ip and request web client
        return {
            "message":"Your request has been successful, a tutor will contact you shortly."
        }


api.add_resource(Form, '/api')

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == "__main__":
    app.run()
