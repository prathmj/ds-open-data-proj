#!/usr/bin/env python2.7

#summarize each new City Council
import string
import os

freqwords = {}
path = "./blackbox/newind/"

#Open results of tfidf run on each new City Council doc
for root, direc, files in os.walk(path):
    for filename in files:
        openpath = path+filename
        with open(openpath,'r') as f:
            lines = f.readlines()
            entry = [line.rstrip() for line in lines]
            entries = [x.split() for x in entry]
            entries.pop(0)
            for i in range(len(entries)):
                freqwords[entries[i][0]] = entries[i][1]

        readpath = "../sam/newtexts/"
        readpath = readpath + filename[0:8] + ".pdf.txt"
        with open(readpath,'r') as j:
            lines = j.read()
            entry = lines.split(". ")
            entry2 = [x.replace("\n", " ") for x in entry]
            entries = [x.split(". ") for x in entry2]

        for sentence in entries:
            words = [x.split(" ") for x in sentence]
            score = 0;
            for word in words[0]:
                if(word.lower() in freqwords.keys()):
                    score+=(int)(freqwords[word.lower()])
            sentence.append(score)

        writepath = "../website/summaries/"+filename[0:8]+".txt"
        with open(writepath, 'w') as k:
            for c, sentence in enumerate(sorted(entries, key=lambda x: x[len(x)-1], reverse = True)):
                if(c >= 10):
                    break
                k.write("{}\n\n".format(sentence[0]))

