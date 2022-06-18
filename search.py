#Copyright (c) 2022 Efe Akaröz
#efeakaroz13@proton.me
#Mr404
import wikipedia
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import threading
from multiprocessing import cpu_count,Pool
import multiprocessing
import time
import json


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
ALLOUTDATA = {"wikipedia":[],"google":[],"yandex":[],"pinterest":[],"torch":[],"imggoogle":[]}


srcsearch= open("keyword.txt","r").read().replace("\n","")


def searchwikipedia(keyword):
	data = []
	result = wikipedia.search(str(keyword), results = 10)
	

	return result

def searchgoogle(keyword):
	output = []
	for i in range(5):

		page = requests.get("https://www.google.com/search?q={}&start={}0".format(keyword.replace(" ","+"),i))
		soup = BeautifulSoup(page.content,"html.parser")
		all_h3= soup.find_all("h3")
		for a in all_h3:
			try:
				data = {
				"title":a.get_text(),
				"url":a.parent.parent.find_all("a")[0].get("href").replace("/url?q=","").split("&")[0]
				}
				output.insert(0,data)
			except:
				pass


	return output


def searchyandex(keyword):
	#searchyandex
	out = []
	
	driver = webdriver.Chrome("./chromedriver",options=chrome_options)

	driver.get("https://yandex.com.tr/search/?text={}".format(keyword.replace(" ","+")))
	soup = BeautifulSoup(driver.page_source,"html.parser")
	all_li= soup.find_all("li")
	for l in all_li:
		try:
			href = l.find_all("a")[0].get("href")
			text = l.get_text()
			try:
				href.split("yandex.com")[1]
			except:
				data = {
				"title":text,
				"url":href
				}
				out.insert(0,data)

		except:
			pass


	return out
def searchpinterest(keyword):
	out = []
	driver = webdriver.Chrome("./chromedriver",options=chrome_options)
	driver.get("https://www.pinterest.com/search/pins/?q="+keyword.replace(" ","+"))
	time.sleep(3)
	soup = BeautifulSoup(driver.page_source,"html.parser")
	images = soup.find_all("img")
	for i in images:
		out.insert(0,i.get("src"))
	return out



def searchtorch(keyword):
	out = []
	proxies = {
	  "http":'socks5h://127.0.0.1:9050',
	  "https":'socks5h://127.0.0.1:9050'
	}
	session = requests.session()
	page = session.get("http://torchdeedp3i2jigzjdmfpn5ttjhthh5wbmda2rr3jvqjg5p77c54dqd.onion/search?query={}&action=search".format(keyword.replace(" ","+")),proxies=proxies,stream=True)
	soup = BeautifulSoup(page.content,"html.parser")
	for h5 in soup.find_all("h5"):
		try:
			data ={
			"title":h5.get_text(),
			"url":h5.find_all("a")[0].get("href")
			}
			out.insert(0,data)
		except:
			pass

	return out




def searchgoogleimages(keyword):
	#searchgoogleimages
	out = []
	page = requests.get("https://www.google.com/search?q={}&tbm=isch".format(keyword.replace(" ","+")))
	soup = BeautifulSoup(page.content,"html.parser")
	all_h3 = soup.find_all("img")
	for a in all_h3:
		try:
			data = {
				"title":a.get("alt"),
				"image":a.get("src"),
				
			}
			out.insert(0,data)

		except Exception as e:
			pass

	return out



def all_job():
	ALLOUTDATA["wikipedia"] = searchwikipedia(srcsearch)
	open("per.txt","w").write(str(int((100/6)*1)))
	ALLOUTDATA["google"] = searchgoogle(srcsearch)
	open("per.txt","w").write(str(int((100/6)*2)))

	
def all_job_2():
	ALLOUTDATA["pinterest"] = searchpinterest(srcsearch)
	open("per.txt","w").write(str(int((100/6)*3)))
	
def all_job_3():
	ALLOUTDATA["imggoogle"] = searchgoogleimages(srcsearch)
	open("per.txt","w").write(str(int((100/6)*4)))
	ALLOUTDATA["yandex"] = searchyandex(srcsearch)
	open("per.txt","w").write(str(int((100/6)*5)))
	ALLOUTDATA["torch"] = searchtorch(srcsearch)
	open("per.txt","w").write(str(int((100/6)*6)))
	
def write_thing():

	json_object = json.dumps(ALLOUTDATA, indent = 4)
  
	# Writing to sample.json
	with open("data.json", "w") as outfile:
	    outfile.write(json_object)



all_job()
all_job_2()
all_job_3()
write_thing()


	


	













