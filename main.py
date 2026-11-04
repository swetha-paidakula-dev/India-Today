import requests 
from bs4 import BeautifulSoup 
import csv 

url = 'https://www.indiatoday.in/' 
res = requests.get(url).content 
soup = BeautifulSoup(res,'html.parser')
#print(soup.prettify())
#a_tag = soup.find_all('a')
#for link in a_tag:
#   print(link.text)


for h3_tag in soup.find_all('h3'):
    for a_tag in h3_tag.find_all('a'):
        print(a_tag.text)
        #print(a_tag.get('href'))
        print(url+a_tag.get('href'))

#url = 'https://www.google.com/'
#res = requests.get(url).content 
#soup = BeautifulSoup(res,'html.parser')
#print(soup.prettify())
#print(soup.a.text)
#print(soup.footer)
#print(soup.script)