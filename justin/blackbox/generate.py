#!/usr/bin/env python2.7

#Open and index every word in the text files of all 2015-2016 meeting docs
#Creates a 'dict'ionary of words and their document frequency

import os
import sys
import string

reg2 = string.ascii_lowercase

path = "../sam/texts/"
count = 0
finalDict = {}

for root, direc, files in os.walk(path):
    for filename in files:
        filename = path+filename
        words = set()
        count = count + 1
        with open(filename, 'r') as f:
            for line in f:
                line = line.split(" ")
                for word in line:
                    string = ""
                    for letter in word:
                        try:
                            letter = letter.lower()
                            if(letter in reg2):
                                string+=letter
                            pass
                        except:
                            print letter,
                            print " was not able to be added to the list"
                    #Don't include "words" with no characters or more than 19
                    #characters, these are likely errors created by the pdf conversion
                    if(len(string) > 0 and len(string) < 20):
                        words.add(string)
        for word in words:
            if word in finalDict:
                finalDict[word] = finalDict[word] + 1
            else:
	        finalDict[word] = 1

with open("./blackbox/dict.txt", 'w') as z:
    for k,v in finalDict.items():
        z.write("{} {}\n".format(k,v))
    z.write("TOTDOCS {}\n".format(count))
