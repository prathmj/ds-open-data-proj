#!/usr/bin/env python2.7
import os
import re
import shutil
import sys
import requests
import csv

def opendatafile(filename):
    with open(filename, 'rb') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quotechar='|')
        first = data.next()
        print "".ljust(74, '=')
        print '|' + first[0].ljust(53) + '|' + first[1].ljust(10) + '|' + first[2].ljust(10) + '|'
        print "".ljust(74, '=')
        for row in data:
            print '|' + row[0].ljust(50) + '|' + row[1].ljust(10) + '|' + row[2].ljust(10) + '|'
        print "".ljust(74, '=')

print("This is a sample program that opens schools.csv file. This csv file comes from the South Bend Open Data website, and contains the names of various schools, the type of school, and the boundary number for the school. It can easily be adapted to open a different open data file and display it in a similar fashion.")

opendatafile('schools.csv')