# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 11:05:26 2018

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from firebase import firebase
import json

url='https://happysorry-2c3e7.firebaseio.com/'
print(url)
fb=firebase.FirebaseApplication(url)

happy=fb.get("/happy",None)
print(happy)

fb.post("/happy",{'sad':{"sadfacce":'cry'}})