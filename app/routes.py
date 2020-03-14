from app import app
from flask import render_template, request
from app.discord import sendDetailsToDiscord
# from app.forms import signinForm
import sys

@app.route('/',methods=["GET"])
@app.route('/index',methods=["GET"])
def index():
    print("Test")
    
    return render_template("index.html")

@app.route('/about',methods=["GET"])
def about():
    return render_template("about.html")

@app.route('/submitted',methods=["GET", "POST"])
def submitted():
    if request.method == 'POST':
        print("TEST TEST TEST")
        sendDetailsToDiscord(request.form['firstname'],request.form['lastname'],request.form['email'],request.form['phone'])
        

    return render_template("submitted.html")