from bs4 import BeautifulSoup
import requests
import unicodedata

url = "https://www.amazon.de/AmazonBasics-hy3-Festplattentasche-schwarz/dp/B003LSTD38?ref_=ast_sto_dp&th=1&psc=1"
HEADERS = { "user-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

def get_product_info(url):
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content,features="lxml")

    try:
        title = soup.find(id='productTitle').get_text().strip()
        print("Produkt: " + title)
    
    except:
        print('failed')

    try:
        soup.select('#availability .a-color-success')[0].get_text().strip()
        available = True
        print('product available')

        payload = {
            'content' : 'Produkt: ' + title + ' ist wieder unter ' + url + ' verfügbar'
        }

        headers = {
            'authorization' : 'NzAyMTMzMDMyODE5MjI4NzMy.YFoGqQ.6Gph8fuNtUQTHJeYuY4VGYe_fio'
        }
        r = requests.post("https://discordapp.com/api/v9/channels/847958015067029547/messages", data = payload, headers=headers)

    except:
        available = False
        print('product not available')

    return title, available


get_product_info(url)
