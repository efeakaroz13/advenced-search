#RSOR

from flask import Flask,render_template,request,redirect,make_response
import os
import subprocess
import requests
import wikipedia
import time
import json
from selenium import webdriver
from bs4 import BeautifulSoup

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
app = Flask(__name__)



@app.route("/view" ,methods=["POST","GET"])
def index():
	data = json.loads(open("data.json","r").read())

	return render_template("index.html",data=data)







@app.route("/check_percentage")
def check_per():
	return {"percentage":open("per.txt","r").read().replace("\n","")}





app.run(debug=True)