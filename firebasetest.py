# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 13:45:31 2018

@author: User
"""
from firebase import firebase
url='https://happysorry-2c3e7.firebaseio.com/'

fb=firebase.FirebaseApplication(url)

fb.post("hello","haha")


