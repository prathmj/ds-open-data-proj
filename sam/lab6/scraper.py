#!/usr/bin/env python2.7

import os
import sys
import re
import requests

url = 'http://data-southbend.opendata.arcgis.com/datasets?q=*&page='

counter = 0
for i in range(1, 7):
    response = requests.get(url + str(i))
    databases = response.json()
    for table in databases['data']:
        counter += 1
        print str(counter) + '\t' + table['name']

query = raw_input('Please select the index of which table you would like to see a description of:\n')

page = int(query)/11 + 1
item = int(query)%10 - 1

data = requests.get(url + str(page)).json()

description = data['data'][item]['description']

print description
