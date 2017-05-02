#!/usr/bin/env python2.7

import PyPDF2
import requests

import os


URL = "http://docs.southbendin.gov/WebLink/PDF/qrr4qmmutv5ow4tnxxodzfng/4/04-14-14%20Common%20Council%20Meeting%20Minutes.pdf"

document = requests.get(URL)

print document.status_code

with open("bandaid.pdf", "wb") as f:
    f.write(document.content)

pdf = PyPDF2.PdfFileReader("bandaid.pdf")
for page in pdf.pages:
    print page.extractText()
