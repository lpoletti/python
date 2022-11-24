import requests
import cfscrape
from bs4 import BeautifulSoup
import re
import pandas as pd
import math

url = "https://www.kabum.com.br/espaco-gamer/cadeiras-gamer"
scraper = cfscrape.create_scraper()

# header = {
#    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"
# }
site = scraper.get(url)
soup = BeautifulSoup(site.content, 'html.parser')
qtd_items = soup.find('div', id='listingCount').get_text().strip()
index = qtd_items.find(' ')
qtd = qtd_items[:index]
ultima_pagina = math.ceil(int(qtd)/20)
dic_produtos = {'url':'','marca' : [], 'preco' : []}

for i in range(1,ultima_pagina+1):
    url_pag = f'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer?page_number={i}&page_size=20&facet_filters=&sort=most_searched'
    site = scraper.get(url_pag)
    soup = BeautifulSoup(site.content, 'html.parser')
    produtos = soup.find_all('div',class_=re.compile('productCard'))

    dic_produtos['url'] = url_pag

    for produto in produtos:
        marca = produto.find('span',class_=re.compile('nameCard')).get_text().strip()
        preco = produto.find('span',class_=re.compile('priceCard')).get_text().strip()
        
        dic_produtos['marca'].append(marca)
        dic_produtos['preco'].append(preco)

df = pd.DataFrame(dic_produtos)
df.to_csv('C:/Users/Luan/Downloads/precos_cadeiras.csv',encoding='utf-8',sep=';')