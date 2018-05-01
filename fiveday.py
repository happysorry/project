# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 18:14:34 2018

@author: User
"""

import datetime
import time
import requests
from io import StringIO
import numpy as np
from pandas_datareader import data # pip install pandas_datareader
import matplotlib.pyplot as plt    # pip install matplotlib
import pandas as pd
a='0'
b='0'
close='0'
fiveday=[]
name=[]
def init(lst,i):
    global a,b,c,e,d,f,g,h,ii,jj,k,l,m,n,o,p
    a=lst['證券代號'].astype(str).values[0]
    b=lst["證券名稱"].astype(str).values[0]
    close=lst["收盤價"].astype(str).values[0]
    fiveday[i].append[close]
    
    

def crawl_price(datestr):
    r = requests.post('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALL')
    df = pd.read_csv(StringIO("\n".join([i.translate({ord(c): None for c in ' '}) 
    for i in r.text.split('\n') 
    if len(i.split('",')) == 17 and i[0] != '='])), header=0)
    return df

    
  
data = {}

for i in range(0,938):
    fiveday.append([])
n_days = 5
date = datetime.date.today().today()

fail_count = 0
allow_continuous_fail_count = 5
while len(data) < n_days:
    datestr=date.strftime("%Y%m%d")
    # 使用 crawPrice 爬資料
    try:
        # 抓資料
        data[datestr] = crawl_price(datestr)
        print('success!')
        #製作圖片表格
        #寫入5天資料
        print(datestr)
        '''
        for i in range(0,937):
            lst=data[datestr][i:i+1]
            init(lst,i)
         
        ''' 
        fail_count = 0
    except:
        # 假日爬不到
        print('fail! check the date is holiday')
        fail_count += 1
        if fail_count == allow_continuous_fail_count:
            raise
            break
    
    # 減一天
    date -= datetime.timedelta(days=1)
    
    print('parsing', datestr)
    time.sleep(10)


print(data[datestr][3:4])




    