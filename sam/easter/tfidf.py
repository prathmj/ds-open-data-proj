#!/usr/bin/env python2.7

import math                         # so we can do math
import requests                     # to get the wikipedia page
import re                           # to search the wikipedia page

def idf(term, collection):          # inverse document frequency for term

    n = collection["TOTDOCS"]       # total number of documents
    if term in collection:          # don't index out of bounds
        return math.log(1 + int(n)/(int(collection[term]) + 1)) # formula
    else:
        return math.log(1 + int(n)) # formula (if term not in collections; = 0)



def tfidf (docName, masterFile):    # computes TF-IDF given title and file
    n = 5                           # how many keywords to return
    ranking = {}                    # dictionary to store tf-idf key:value
    collection = tfidf_load(masterFile) # put the file into a dictionary

    docName = docName.replace(" ", "_") # turn all spaces to _ (text->html)
    document = tfidf_wc(docName)        # get a dictionary of word:wordcount

    # compute the TF-IDF for each word in the document
    for word, count in document.items():
        ranking[word] = ((1 + math.log(int(count))) * idf(word, collection))

    # sort the values from greatest TF-IDF (most important) to least
    output = []
    for rank, word in enumerate(sorted(ranking, key=ranking.get, reverse=True)):
        if rank >= n:               # only give me n keywords
            break
        output.append(word)         # append the important keyword

    return output                   # return a list of keywords

def tfidf_load(filename):           # loads data from a file into a dictionary
    output = {}
    with open(filename) as f:       # open filename; close it after loop ends
        lines = f.readlines()       # a list where every element is a line
        entry = [line.rstrip() for line in lines]   # strip newline
        entries = [x.split() for x in entry]        # turn every line into a list of words
        for i in range(len(entries)):               # for every line
            output[entries[i][0]] = entries[i][1]   # key is first word, value is second word

    return output                   # return dictionary

def tfidf_wc(docName):              # wordcount for every word in docName
    docName = docName.replace("_", "%20")   # turn htmlName->JSONname
    reg = '[A-Za-z]+'                       # regex to find words

    try:                            # format the url
        url = 'https://en.wikipedia.org/w/api.php?action=query&titles={}&prop=revisions&rvprop=content&format=json'.format(docName)
        pass
    except:                         # catch incorrect webpages
        print "error that's not a webpage"

    # travel down the json to the relevant data
    r = requests.get(url)           # get the website data
    r = r.json()                    # view it as json data
    r = r['query']                  # move to the query field
    r = r['pages']                  # move to the pages field
    r = r[r.keys()[0]]              # move to the fist field (unique page id)
    r = r['revisions']              # move to the revisions field
    r = r[0]                        # move to the first (usually only) revision
    r = r['*']                      # move to the * field which holds the text

    ret = re.findall(reg, r)        # get a list of all words in the article
    wordCount = {}                  # dictionary to return
    for word in ret:                # for every word we found
        word = word.lower()         # make it lowercase for comparison
        wordCount.setdefault(word, 0)   # if word isn't a key, set it's value to0
        wordCount[word] += 1        # increment the word count of that word

    return wordCount                # return the dictionary
