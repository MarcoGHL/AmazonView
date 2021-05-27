from bs4 import BeautifulSoup
import requests
import unicodedata

url = "https://www.amazon.de/Sony-Interactive-Entertainment-PlayStation-5/dp/B08H93ZRK9/ref=sr_1_2?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=ps5&qid=1622147092&sr=8-2"
HEADERS = ({'User-Agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"})

def get_product_info(url):
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content,features="lxml")

    try:
        title = soup.find(id='productTitle').get_text().strip()
        print("Produkt: " + title)
    
    except:
        print('failed')

get_product_info(url)
