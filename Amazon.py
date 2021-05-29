from bs4 import BeautifulSoup
import requests
import unicodedata
import win32gui, win32con

url = "https://www.amazon.de/Sony-Interactive-Entertainment-PlayStation-5/dp/B08H93ZRK9/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=ps5&qid=1622285903&sr=8-1"
HEADERS = { "user-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

def get_product_info(url):
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content,features="lxml")

    try:
        title = soup.find(id='productTitle').get_text().strip()
    
    except:
        print('failed')

    try:
        soup.select('#availability .a-color-success')[0].get_text().strip()
        available = True

        payload = {
            'content' : 'Produkt: ' + title + ' ist wieder unter ' + url + ' verfügbar'
        }

        headers = {
            'authorization' : 'NzAyMTMzMDMyODE5MjI4NzMy.YLFyHw.BbjaiRJe2yoyqaxsShqeDgU0JPo'
        }
        r = requests.post("https://discordapp.com/api/v9/channels/847958015067029547/messages", data = payload, headers=headers)

    except:
        available = False
        print('product not available')

    return title, available


get_product_info(url)
