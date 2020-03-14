from app import app
from flask import render_template, request, Response
from app.discord import sendDetailsToDiscord
import sys

@app.route('/',methods=["GET"])
@app.route('/index',methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/about',methods=["GET"])
def about():
    return render_template("about.html")

@app.route('/submitted',methods=["GET", "POST"])
def submitted():
    if request.method == 'POST':
        sendDetailsToDiscord(request.form['firstname'],request.form['lastname'],request.form['email'],request.form['phone'])
    if Response.status_code == 404:
        return render_template("error.html",error = 404)

    return render_template("submitted.html")