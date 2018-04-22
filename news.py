# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 15:15:10 2018

@author: User
"""
import requests
from bs4 import BeautifulSoup
base_url = "https://tw.news.yahoo.com"
url = "https://tw.news.yahoo.com/finance/archive/"
response=requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
srcset=soup.find_all("srcset")
da=list()
da=response.text.split('img srcset="" class="')
for i in range (len(da)):
    print(i)
print(da[1])