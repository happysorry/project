# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 01:10:07 2018

@author: User
"""

import requests
import time
from firebase import firebase
import matplotlib.pyplot as plt
import sched



url='https://happysorry-2c3e7.firebaseio.com/'

fb=firebase.FirebaseApplication(url)   
t=time.time()

url="http://mis.twse.com.tw/stock/api/getChartOhlc.jsp?ex=tse&ch=t00.tw&fqy=5&delay=0&_={0}".format(int(round(t * 1000)))
res = requests.get(url)
data=res.text
'''切出info'''
list1=data.split("infoArray")
'''info分類'''
list2=list1[1].split(",")

o=""
l=""
h=""
v=""
z=""
y=""
u=""
w=""
d=""
ip=""
"""
d：今日日期，ex. 20150224
h：今日最高，ex. 42.90
l：今日最低，ex. 42.35
o：開盤價，ex. 42.40
u：漲停點，ex. 45.10
w：跌停點，ex. 39.20
y：昨收，ex. 42.15
z：最近成交價，ex. 42.85
v：Volume，當日累計成交量，ex. 11608
ip：好像是一個 flag，3 是暫緩收盤股票, 2 是趨漲, 1 是趨跌， ex. 0
"""
'''切檔案'''
for i in list2:
   if(not i.find('"l":"')):
       string=i.split('"')
       l=string[3]
   if(not i.find('"o":')):
       string=i.split('"')
       o=string[3]
   if(not i.find('"h":')):
       string=i.split('"')
       h=string[3] 
   if(not i.find('"v":')):
       string=i.split('"')
       v=string[3]    
   if(not i.find('"z":')):
       string=i.split('"')
       z=string[3]    
   if(not i.find('"y":')):
       string=i.split('"')
       y=string[3]    
   if(not i.find('"u":')):
       string=i.split('"')
       u=string[3]    
   if(not i.find('"w":')):
       string=i.split('"')
       w=string[3]
   if(not i.find('"d":')):
       string=i.split('"')
       d=string[3]
   if(not i.find('"ip":')):
       string=i.split('"')
       ip=string[3] 
       

print(d)
'''minus=漲跌差價'''
minus=round(float(z)-float(y),3)
'''漲跌百分比'''
percent=round(minus/float(y)*100,2)
percent1=str(percent)+'%'

'''更新firebase'''
def addfire():
    data={"今日日期":d,"今日最高":h,"今日最低":l,"開盤價":o,"漲停點":u,"跌停點":w,"昨收":y,"最近成交價":z,"當日累計成交量":v,"ip flag":ip,"漲跌差價":minus,"百分比":percent1}
    fb.post("/today",data)

def deletetoday():
    fb.delete("","today")
    
def addz():
    fb.post("/z",z)

def delz():
    fb.delete("","/z")

data1=list()
data2=list()
'''獲取Z資料'''
def getz():
    res1=fb.get("/z",None)
    for i in res1:
        temp=i.split("'")
        for j in range(len(temp)):
            data1.append(temp[j])
            
def picturez():
    for i in data1:
        string="/z/{0}".format(i)
        data2.append(fb.get(string,None))
    plt.plot(data2)
    plt.show()
    
if __name__ == '__main__':   
    while True:
        time.sleep(30)
        deletetoday()
        addfire()
        
'''
getz()
picturez()
'''
