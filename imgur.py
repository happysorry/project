# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 15:18:35 2018

@author: User
"""

from imgurpython import ImgurClient


def upload_photo(image_url):
    client_id = 'happysorry34'
    client_secret = 'jeff81397'
    access_token = 'your token'
    refresh_token = 'your token'
    client = ImgurClient(client_id, client_secret, access_token, refresh_token)
    album = None # You can also enter an album ID here
    config = {
  'album': album,
 }

    print("Uploading image... ")
    image = client.upload_from_url(image_url, config=config, anon=False)
    print("Done")    
    return image['link']