from flask import Flask,render_template,request,redirect,make_response
import os
import subprocess
import requests
import wikipedia
import time
from selenium import webdriver
from bs4 import BeautifulSoup

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
app = Flask(__name__)
@app.route("/")
def index():
	return render_template("index.html")


@app.route("/pin")
def pin():
	def searchpinterest(keyword):
		driver = webdriver.Chrome("./chromedriver",options=chrome_options)
		driver.get("https://www.pinterest.co.uk/search/pins/?q="+keyword.replace(" ","+"))
		driver.execute_script("document.scrollingElement.scrollTo(0,500)")
		driver.execute_script("document.scrollingElement.scrollTo(0,600)")
		driver.execute_script("document.scrollingElement.scrollTo(0,600)")
		time.sleep(1)
		soup = BeautifulSoup(driver.page_source,"html.parser")
		images = soup.find_all("img")

		return images
	return str(searchpinterest("newyork"))

app.run(debug=True)