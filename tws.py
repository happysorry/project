# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 14:10:53 2018

@author: User
"""

from imgurpython import ImgurClient
import pyimgur
client_id = '290c05b6ac55301'
client_secret = '3b06b845e9682b0a294b3d494a48d84d8155503b'
path="C:\\Users\\User\\Desktop\\me.jpg"
client = ImgurClient(client_id, client_secret)
auth=client.get_auth_url('pin')

al=client.get_account_album_ids("happysorry")
client.upload_from_path(path,config=None,anon=True)
print(al)