# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:32:03 2018

@author: User
"""
from firebase import firebase
url='https://happysorry-2c3e7.firebaseio.com/'

fb=firebase.FirebaseApplication(url)   
fb.post("\good","yaya")

fb.delete("","\good")