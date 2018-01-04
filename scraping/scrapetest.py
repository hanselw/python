from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
'''
from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())



#html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
html = urlopen("http://www.baidu.com/index.html")

bsObj = BeautifulSoup(html.read())
print(bsObj.h1)
'''

def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read())
		title = bsObj.body.h1
	except AttributeError as e:
		return None
	return title
'''
title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
if title == None:
	print("Title could not be found")
else:
	print(title)
'''

'''
htmlwarandpeace = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")



bsObj = BeautifulSoup(htmlwarandpeace)

nameList = bsObj.findAll("span",{"class":"green"})

 for name in nameList:
	print(name.get_text())


htmlpage3 = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObjpage3 = BeautifulSoup(htmlpage3)
for child in bsObjpage3.find("table",{"id":"giftList"}).tr:
	print(child)
'''


# http://en.wikipedia.org/wiki/Kevin_Bacon
url = "http://en.wikipedia.org/wiki/Kevin_Bacon"
html = urlopen(url)
bsObj = BeautifulSoup(html)

def findahref(a):
	for link in a.findAll("a"):
		if 'href' in link.attrs:
			print(link.attrs['href'])


def findahrefregex(b):
	try:
		for link in b.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
			if 'href' in link.attrs:
				print(link.attrs['href'])
	except Exception as e:
		raise e


#findahref(bsObj)
findahrefregex(bsObj)


