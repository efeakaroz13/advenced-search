from flask import Flask,render_template,request,redirect,make_response
import os
import subprocess
import requests
import wikipedia

app = Flask(__name__)
@app.route("/")
def index():
	return render_template("index.html")

app.run(debug=True)