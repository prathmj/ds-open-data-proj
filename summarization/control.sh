#!/bin/sh

#This automates the generation of summaries
./blackbox/generate.py
./blackbox/driver.py
./blackbox/summarize.py
rm ./blackbox/dict.txt


#Once pdfs are being downloaded automatically, uncomment these

#Move text files from ../sam/newtexts to ../sam/texts, they'll be used to improve the diversity of dict.txt

#Remove converted pdfs
#rm ../sam/pdfs/*.pdf

#Clean out indexes of documents previously summarized
#rm ./blackbox/newind/*.txt

#New pdf is added to ../sam/newpdfs run textify to get new text ripped from new pdf
# ../sam/textify.py





