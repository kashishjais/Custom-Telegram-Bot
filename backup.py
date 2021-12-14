# Init
newsapi = NewsApiClient(api_key='18b3064537594d28bccda78d7c20c1a7')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='in')

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.in,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/top-headlines/sources
sources = newsapi.get_sources()
print(top_headlines)

import requests

url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2021-12-14&'
       'sortBy=popularity&'
       'apiKey=18b3064537594d28bccda78d7c20c1a7')

response = requests.get(url)

print(response.json())
