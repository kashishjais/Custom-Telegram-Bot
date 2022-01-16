import requests
import constants as keys
def news():
	main_url="https://newsapi.org/v2/top-headlines?country=in&apiKey="+keys.news_API
	news=requests.get(main_url).json()
	article=news["articles"]
	news_article=[]
	heads=[]
	for arti in article:
		news_article.append(arti['title'])
	for i,arti in enumerate(news_article):
		heads.append(f'📌{i}-->{arti}\n')
	return heads	
	
def business_news():
	main_url="https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey="+keys.news_API
	news=requests.get(main_url).json()
	article=news["articles"]
	news_article=[]
	heads=[]
	for arti in article:
		news_article.append(arti['title'])
	for i,arti in enumerate(news_article):
		heads.append(f'💸{i}-->{arti}\n')
	return heads	

def entertainment_news():
	main_url="https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey="+keys.news_API
	news=requests.get(main_url).json()
	article=news["articles"]
	link=news["url"]
	news_article=[]
	heads=[]
	for arti in article:
		news_article.append(arti['title'])
	for i,arti in enumerate(news_article):
		heads.append(f'💃🏻{i}-->{arti}\n')
	heads.append(link)	
	return heads
		

def technology_news():
	main_url="https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey="+keys.news_API
	news=requests.get(main_url).json()
	article=news["articles"]
	news_article=[]
	heads=[]
	for arti in article:
		news_article.append(arti['title'])
	for i,arti in enumerate(news_article):
		heads.append(f'👩🏻‍💻{i}-->{arti}\n')
	return heads	

def science_news():
	main_url="https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey="+keys.news_API
	news=requests.get(main_url).json()
	article=news["articles"]
	news_article=[]
	heads=[]
	for arti in article:
		news_article.append(arti['title'])
	for i,arti in enumerate(news_article):
		heads.append(f'📚{i}-->{arti}\n')
	return heads	

def sports_news():
	main_url="https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey="+keys.news_API
	news=requests.get(main_url).json()
	article=news["articles"]
	news_article=[]
	heads=[]
	for arti in article:
		news_article.append(arti['title'])
	for i,arti in enumerate(news_article):
		heads.append(f'🎯{i}-->{arti}\n')
	return heads	

