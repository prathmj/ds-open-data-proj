#!/usr/bin/env python2.7

#indexes every word of new council minutes
#these are the docs we will be summarizing

import sys
import os
import tfidf

path = "./newtexts/"
for root, direc, files in os.walk(path):
    #touch every file we want to summarize
    #send to tfidf function
    for filename in files:
        writepath = "./blackbox/newind/"
        writepath = writepath+filename[0:8]+".txt"
        readpath = path+filename
        output = tfidf.tfidf(readpath, "./blackbox/dict.txt")

        #The first entry is an empty string, pop it
        output.pop("", None)

        #write each file's word uniqueness scoring to a file for summarization.py
        with open(writepath, "w") as f:
            for word, count in output.items():
                f.write("{} {}\n".format(word, count))
