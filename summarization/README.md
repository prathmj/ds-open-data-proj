This will provide an explanation of how the files in this folder create summarization documents.

To start, we must extract plain text from the South Bend City Council's PDF meeting documents. textify.py analyzes a recent PDF we wish to summarize found in newpdfs/ and writes the text file to /newtexts

In order to run the text frequency-inverse document frequence algorithm, one must create a dictionary of words from multiple documents. In order to get as accurate summarizations as possible, we selected all of the City Council meeting PDFs from 2015 and 2016. The language in these documents should be similar to the documents we wish to summarize so we will not have sytanx bias in our results. Common words throughout the meeting minutes which might otherwise be pretty unique
will get filtered out.

To create this master dictionary, generate.py opens every file in the texts/ folder and analyzes every word in each document. The words from these documents are indexed in a python dictionary. The set of words for an individual document are stored in an unordered set. Every word is added to this unordered set, so we have a collection of each word within a single document. Then, for each word in this set, if it exists as a key in the dictionary, then the value is incremented by
1. If the word isn't already in the dictionary then it is added and the value is set to 1. This final dictionary contains every individual word and the number of documents it appeared in. This dictionary is written to a .txt file, along with the total count of documents analyzed, and this dictionary is used to run the tfidf algorithm.

The driver.py program steps through every document in the newtexts/ folder and sends the file's address and the address of the master dictionary to the tfidf class. A dictionary contiaining every word in the newtexts/ document is returned, with the weighting of uniqueness as the value. The uniqueness values are written to a text file with the name of the date of the originally published pdf.

The tfidf.py program opens the newtexts/ document and indexes every word in the document using a dictionary. The dictionary of words and document counts stored in the dictionary created by generate.py is loaded into a dictionary. The term frequency-inverse document frequency algorithm scores the words from the single document based on the frequency of that word in other documents. More unique words receive a higher scoring as determined by the function idf. The scorings are stored as the
value in the single document dictionary. This dictionary is returned to the driver program.

Finally, the summarize.py reads each index document created by driver.py and stores these values in a dictionary. Then, each sentence in the original text document corresponding to a certain index file in newind/ is read in and stored in a list of lists. So each sentence is stored within a list, and each of those lists is wrapped in a list. We step through every entry of the list, extract every word from the sentence string, and cross-reference that word with the
uniqueness score stored in the index dictionary. The sum of all the words in the sentences is appended to the lower list. Now we have [ [sentence, totalScore], [sentence, totalScore],...], and we order the encompassing list in descending order by totalScore and return the top 10 sentences. These are written to a text file in /website/summarization so they can be accessed by users.

We chose to use dictionaries for our word indexing because they have a constant look-up time, automatically threw out the issue of duplication, and allowed us to maintain the association with counts and weights.
