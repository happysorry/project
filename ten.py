# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 14:56:45 2018

@author: User
"""
import requests
import firebase_admin
from firebase_admin import credentials,auth
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('C:\\Users\\User\\Desktop\\pro\\json\\happysorry-70532e6201e9.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://happysorry-2c3e7.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
