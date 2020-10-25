
# importing required libraries for web scraping
import requests
import nltk
from bs4 import BeautifulSoup
import requests
import lxml
from nltk import *
import pandas as pd


## For this example, we are going scrape Flipkart website to extract the Price, Name, and Rating of Laptops.

products=[] #List to store name of the product
prices=[] #List to store price of the product

links1=[] #List to store links of the page

# url for website
url='https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2'

# defifing functions for web scraping

def  getLinks (url):
    html=requests.get(url)
    html_page=html.text
    soup = BeautifulSoup(html_page, 'lxml')
    Links = []
    for link in soup.find_all('a', href=True, text=True):
        Links.append(link.get('href'))

    return Links
all_links=getLinks(url)

def getText(url):
    html = requests.get(url)
    html_page = html.text
    soup = BeautifulSoup(html_page, 'lxml')
    texts1=[]
    for text in soup.find_all('p'):
        texts1.append(text.getText().strip())

    return texts1

def getTitle(url):
    html = requests.get(url)
    html_page = html.text
    soup = BeautifulSoup(html_page, 'lxml')
    return (soup.find('title').string)


content = requests.get(url).text
soup = BeautifulSoup(content,features="lxml")
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    products.append(name)
    prices.append(price)


#       saving information in csv file for structured data collection

df = pd.DataFrame({'Product Name':products,'Price':prices})
df.to_csv('products.csv', index=False, encoding='utf-8')



print(" ***   Website Title   *** \n")
print(getTitle(url))

print(" ***   Products   *** \n")
print(products)

print(" ***   Prices   *** \n")
print(prices)

print(" ***   Links of website   *** \n")
print(all_links)