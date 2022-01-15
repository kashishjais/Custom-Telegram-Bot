import requests
import constants as keys
def news():
	main_url="https://newsapi.org/v2/top-headlines?country=in&apiKey="+keys.news_API
	news=requests.get(main_url).json()
	article=news["articles"]
	news_article=[]
	for arti in article:
		news_article.append(arti['title'])
	for i,arti in enumerate(news_article):
		return news_article
	
def business_news():
	main_url="https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey="+keys.news_API
	news=requests.get(main_url).json()
	article=news["articles"]
	news_article=[]
	for arti in article:
		news_article.append(arti['title'])
	return news_article

def entertainment_news():
	main_url="https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey="+keys.news_API
	news=requests.get(main_url).json()
	article=news["articles"]
	news_article=[]
	for arti in article:
		news_article.append(arti['title'])
	return news_article

def technology_news():
	main_url="https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey="+keys.news_API
	news=requests.get(main_url).json()
	article=news["articles"]
	news_article=[]
	for arti in article:
		news_article.append(arti['title'])
	return news_article	

def science_news():
	main_url="https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey="+keys.news_API
	news=requests.get(main_url).json()
	article=news["articles"]
	news_article=[]
	for arti in article:
		news_article.append(arti['title'])
	return news_article	

def sports_news():
	main_url="https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey="+keys.news_API
	news=requests.get(main_url).json()
	article=news["articles"]
	news_article=[]
	for arti in article:
		news_article.append(arti['title'])
	return news_article	

