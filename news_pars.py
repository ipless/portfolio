from logging import exception
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time


count=0
url = "https://ria.ru/"
response = requests.get(url, headers={'User-Agent': UserAgent().chrome})
tree = BeautifulSoup(response.content, 'html.parser')

news = tree.find_all('div', {'class' : 'cell-extension__item-bg'})
links=tree.find_all('a', {'class' : 'cell-extension__item-link'})

f = open('parse.csv','w',encoding='ANSI')
for link in links:
    try:
        url = "https://ria.ru"
        if 'http' in link.get('href'):
            print(link.get('href'))
            url2=str(link.get('href'))
            response = requests.get(url2, headers={'User-Agent': UserAgent().chrome})
            cat_tree = BeautifulSoup(response.content, 'html.parser')
            cat_news = cat_tree.find_all('span', {'class' : 'cell-list__item-title'})
            cat_time = cat_tree.find_all('span', {'class' : 'elem-info__date'})
            count=0
            while count<len(cat_news):
                f.write(f'{cat_news[count].text}, {cat_time[count].text}\n')
                print('записал')
                count+=1 
            print(response)
            time.sleep(1)
        else: 
            print(link.get('href'))
            url2=url+str(link.get('href'))
            print(url2)
            response = requests.get(url2, headers={'User-Agent': UserAgent().chrome})
            cat_tree = BeautifulSoup(response.content, 'html.parser')
            cat_news = cat_tree.find_all('div', {'class' : 'list-item__content'})
            cat_time = cat_tree.find_all('div', {'class' : 'list-item__date'})
            count=0
            while count<len(cat_news):
                f.write(f'{cat_news[count].text}, {cat_time[count].text}\n')
                print('записал')
                count+=1 
            print(response)
            time.sleep(1)
    except:
        print(exception)
f.close()

    
