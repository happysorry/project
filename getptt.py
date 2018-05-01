# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 15:45:18 2018

@author: User
"""

import requests
from bs4 import BeautifulSoup
from firebase import firebase
import matplotlib.pyplot as plt



url = 'https://www.ptt.cc/bbs/Stock/index.html'


'''0:最舊,1:上頁,2:下頁,3:最新'''     
'''2、3不一定有可能沒有下一頁'''   
page=list()
titles=list()
newurl=list()


def getpage(url):
    page.clear()
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    art=soup.find_all('a','btn wide')
    for i in art:
        try:
            string=str(i)
            list1=string.split('"')
            temp='https://www.ptt.cc{0}'.format(list1[3])
            page.append(temp)
        except:
            print("None")


def getnews(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    articles = soup.find_all('div', 'r-ent')
    
    for article in articles:
        try:
            meta = article.find('div', 'title').find('a')
            title = meta.getText().strip()
            link = meta.get('href')
            push = article.find('div', 'nrec').getText()
            date = article.find('div', 'date').getText()
            author = article.find('div', 'author').getText()
            newsurl=meta.get('href')
            news='https://www.ptt.cc{0}'.format(newsurl)
            if not title.find('[新聞]'):
                titles.append(title)
                newurl.append(news)
                addfire(title,news)
                print(push, title, date, author)  # result of setp-3
        except:
            print("Noneasdasd")
            

def addfire(a,b):
    url='https://happysorry-2c3e7.firebaseio.com/'
    fb=firebase.FirebaseApplication(url) 
    data={"標題":a,"url":b}
    fb.post("/news",data)

def deletenews():
    url='https://happysorry-2c3e7.firebaseio.com/'
    fb=firebase.FirebaseApplication(url) 
    fb.delete("","news")



if __name__ == '__main__':
    deletenews()
    getnews(url)
    getpage(url)
    while len(titles)<20:
        getnews(page[1])
        getpage(page[1])
        
        
        
        

    