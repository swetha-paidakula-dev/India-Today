import requests 
from bs4 import BeautifulSoup 
import csv 

#  INDIA TODAY 
#url = 'https://www.indiatoday.in/' 
#res = requests.get(url).content 
#soup = BeautifulSoup(res,'html.parser')
#print(soup.prettify())
#a_tag = soup.find_all('a')
#for link in a_tag:
#   print(link.text)


# for h3_tag in soup.find_all('h3'):
#     for a_tag in h3_tag.find_all('a'):
#         print(a_tag.text)
#         #print(a_tag.get('href'))
#         print(url+a_tag.get('href'))


#  GOGLE PAGE
#url = 'https://www.google.com/'
#res = requests.get(url).content 
#soup = BeautifulSoup(res,'html.parser')
#print(soup.prettify())
#print(soup.a.text)
#print(soup.footer)
#print(soup.script)


#  FLIPKART 

import json

# Product URL
url = 'https://www.flipkart.com/intelligent-investor/p/itmfbqhvgjgsee2q'
res = requests.get(url).content
soup = BeautifulSoup(res, 'html.parser')

# Extract Title
title = soup.find('h1', class_='v1zwn21n v1zwn27 _1psv1zeb9 _1psv1ze0')
print('Title:', title.text)

# Extract Price
price = soup.find('div', class_='v1zwn21n v1zwn20 _1psv1zeb9 _1psv1ze0')
print('Price:', price.text)

# Extract JSON data
data = soup.find('script', id='jsonLD').text

#print(data)

context = json.loads(data)

#print(context)
#print(len(context))

print(context[0])
print(context[0]['@context'])

print('review_count:', context[0]['aggregateRating']['reviewCount'])

print('Rating:', context[0]['aggregateRating']['ratingValue'])