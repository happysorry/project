# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 17:22:04 2018

@author: User
"""
from google.auth import environment_vars
from google.auth import exceptions
import google.auth.transport._http_client
from google.cloud import storage
import os
from google.auth import compute_engine

credentials = compute_engine.Credentials()

# Create the client using the credentials and specifying a project ID.
client = storage.Client(credentials=credentials, project="happy")
buckets = list(client.list_buckets())
print(buckets)