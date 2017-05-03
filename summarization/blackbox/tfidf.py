#!/usr/bin/env python2.7

import math                         # so we can do math

def idf(term, collection):          # inverse document frequency for term

    n = collection["TOTDOCS"]       # total number of documents
    if term in collection:          # don't index out of bounds
        return math.log(1 + int(n)/(int(collection[term]) + 1)) # formula
    else:
        return math.log(1 + int(n)) # formula (if term not in collections; = 0)



def tfidf (docName, masterFile):    # computes TF-IDF given title and file
    n = 100                          # how many keywords to return
    ranking = {}                    # dictionary to store tf-idf key:value
    collection = tfidf_load(masterFile) # put the file into a dictionary

    docName = docName.replace(" ", "_") # turn all spaces to _ (text->html)
    document = tfidf_wc(docName)        # get a dictionary of word:wordcount

    # compute the TF-IDF for each word in the document
    for word, count in document.items():
        ranking[word] = ((1 + math.log(int(count))) * idf(word, collection))

    # sort the values from greatest TF-IDF (most important) to least
    output = {}
    for rank, word in enumerate(sorted(ranking, key=ranking.get, reverse=True)):
        if rank >= n:               # only give me n keywords
            break
        output[word] = document[word]         # append the important keyword

    return output                   # return a list of keywords

def tfidf_load(filename):           # loads data from a file into a dictionary
    output = {}
    with open(filename) as f:       # open filename; close it after loop ends
        lines = f.readlines()       # a list where every element is a line
        entry = [line.rstrip() for line in lines]   # strip newline
        entries = [x.split() for x in entry]        # turn every line into a list of words
        entries.pop(0)
        for i in range(len(entries)):               # for every line
            output[entries[i][0]] = entries[i][1]   # key is first word, value is second word

    return output                   # return dictionary

def tfidf_wc(docName):              # wordcount for every word in docName
    import string
    alph = string.ascii_lowercase
    wordCount = {}                  # dictionary to return
    with open(docName, 'r') as f:
        ret = f.readlines();
    for line in ret:                # for every word we found
        line = line.split(" ")
        for word in line:
            string = ""
            for letter in word:
                letter = letter.lower()
                if(letter in alph):
                    string+=letter
            wordCount.setdefault(string, 0)   # if word isn't a key, set it's value to0
            wordCount[string] += 1        # increment the word count of that word
    return wordCount                # return the dictionary
