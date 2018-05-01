# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 17:56:59 2018

@author: User
"""

import pyimgur
client_id = '290c05b6ac55301'
im = pyimgur.Imgur(client_id)
path="C:\\Users\\User\\Desktop\\me.jpg"

uploaded_image = im.upload_image(path, title="Uploaded with PyImgur")
print(uploaded_image.title)
print(uploaded_image.link)
print(uploaded_image.size)
print(uploaded_image.type)