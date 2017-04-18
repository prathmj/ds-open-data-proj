#!/usr/bin/env python2.7

import requests
import os
import sys
import re
import string

#make request
addy = 'http://top.hatnote.com/'

#headers  = {'user-agent': 'reddit-{}'.format(os.environ['USER'])}
response = requests.get(addy)

#if(response.status_code == 404):
#  print "The {} was not found :(".format(sub)
response = response.text
reg = '.*<a class.*https://en.wikipedia.org/wiki/([^"]*)'
pat = re.findall(reg, response)

#filter Wiki pages for text
reg2 = '[A-Za-z]+'
sets = []
for element in pat:
  element = element.replace("_","%20")
  try:
  	url = 'https://en.wikipedia.org/w/api.php?action=query&titles={}&prop=revisions&rvprop=content&format=json'.format(element)
	r = requests.get(url)
 	pass
  except:
#	print element,
#  	print " was not able to be searched due to character encoding problems."
	continue
  r = r.json()
  r = r['query']
  r = r['pages']
  r = r[r.keys()[0]]
  r = r['revisions']
  r = r[0]
  r = r['*']
  ret = re.findall(reg2,r)  
  words = set()
  for word in ret:
    words.add(word.lower())	
  sets.append(words)

finalDict = {}
for element in sets:
  for word in element:
	if word in finalDict:
	  finalDict[word] = finalDict[word] + 1
	else:
	  finalDict[word] = 1
#print finalDict

for k,v in finalDict.items():
  print '{} {}'.format(k,v)
	
print "TOTDOCS {}".format(len(sets))
