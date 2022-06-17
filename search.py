import wikipedia
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')

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
				"url":a.parent.parent.find_all("a")[0].get("href").replace("/url?q=","")
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
	driver.get("https://www.pinterest.co.uk/search/pins/?q="+keyword.replace(" ","+"))
	soup = BeautifulSoup(driver.page_source,"html.parser")
	images = soup.find_all("img")
	for i in images:
		out.insert(0,i.get("src"))
	return out



def searchtorch(keyword):
	#searchtorch

	pass


def searchstackoverflow(keyword):
	#searchstackoverflow

	pass

def searchgoogleimages(keyword):
	#searchgoogleimages

	pass



print(searchpinterest("Lana del rey"))