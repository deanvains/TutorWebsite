import sys
import os

import requests
import yagmail

from flask import Flask, render_template, request, Response, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

import config


app = Flask(__name__)
api = Api(app)
CORS(app)


def sendDetailsToEmail(name, email, phone, state, course, address, browser):

    message = createMessage(name, email, phone, state, course, address, browser)
    with yagmail.SMTP(config.email, config.phrase) as yag:
        contents = [message]
        yag.send('lachie.russell@gmail.com', 'New Client', contents)


def createMessage(name, email, phone, state, course, address, browser):
    str = f"""
        Hello Tutors,
        
        My name is {name} and I would like to apply for tutoring in {course}.
        
        State: {state}
        My email address is: {email}
        My phone number is: {phone}
        
        Browser: {browser}
        IP:      {address}
    """
    return str
    

@app.route('/submitted', methods=["POST"])
def submitted():
    try:
        sendDetailsToEmail(
            request.form['name'],
            request.form['email'],
            request.form['phone'],
            request.form['state'],
            request.form['course'],
            request.environ['REMOTE_ADDR'],
            request.headers.get('User-Agent')
        )
    except:
        return "Error", 400
    return "Success", 200


@app.route('/submitted', methods=["GET"])
def get():
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


if __name__ == "__main__":
    app.run(port="59191")
