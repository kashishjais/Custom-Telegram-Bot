import requests
import constants as keys
def news():
	main_url="https://newsapi.org/v2/top-headlines?country=in&apiKey="+keys.news_API
	news=requests.get(main_url).json()
	article=news["articles"]
	news_article=[]
	for arti in article:
		news_article.append(arti['title'])
	return news_article
	for i in range(len(news_article)):
		print(i+1,news_article[i])	

