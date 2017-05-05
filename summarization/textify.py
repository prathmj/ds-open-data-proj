#!/usr/bin/env python2.7

"""
I found this function online at http://stackoverflow.com/questions/26494211/extracting-text-from-a-pdf-file-using-pdfminer-in-python but the driver at the bottom was written by me.
"""

import os


from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text



pdfs = "./newpdfs/"
texts = "./newtexts/"
for root, dirs, files in os.walk(pdfs):         # get a list of files in pdfs
    for filename in files:                      # for every file in that list
        text = texts + filename + ".txt"        # the path to write to
        pdf = pdfs + filename                   # the path to read from
        print "ripping ", pdf, "..."            # for readibility when running

        with open(text, 'w') as f:              # open the file to write to
            f.write(convert_pdf_to_txt(pdf))    # use the function to convert
