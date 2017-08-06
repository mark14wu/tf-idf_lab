import sys
import string
import re

import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import *
sentence = "I am a boy, you are a girl. but I do not know that person's gender."

"""
tokens = nltk.pos_tag(word_tokenize(re.sub("[^a-zA-Z0-9]", " ", sentence.lower())))
print(tokens)
"""


lmtzr = WordNetLemmatizer()

"""
tokens = lmtzr.lemmatize("am",'n')
print(tokens)
"""

document = list()
#print(tokens)

def get_pos(tag):
    start = tag[0]
    if start == "J":
        return "a"
    elif start == "V":
        return "v"
    elif start == "N":
        return "n"
    elif start == "R":
        return "r"
    else:
        return 'n'

file_object = open('file.1','r')
lines = file_object.readlines()

file_object.close()

file_stop = open('stopwords1.txt', 'r')
stopwords = file_stop.read()
file_stop.close()


start_doc = False
doc_count = 0
for i in lines:
    clear_line = i.strip()
    if clear_line == "":
        continue
    elif clear_line[0:5] == "<DOC>" and len(clear_line) == 5:
        if start_doc == False:
            start_doc = True
            new_doc = dict()
            document.append(new_doc)
    elif clear_line[0:6] == "</DOC>":
        start_doc = False
        doc_count += 1
    elif clear_line[0:7] == "<DOCNO>" :
        continue
    elif clear_line[0:7] == "<title>":
        continue
    elif clear_line[-8:] == "</title>":
        continue
    else:
        line = ""
        if clear_line[0:9] == "<speaker>":
            line = " ".join( clear_line.split()[1:] )
        else:
            line = clear_line
        tokens = nltk.pos_tag(word_tokenize(re.sub("[^a-zA-Z0-9]", " ", line.lower())))
        #print(tokens)
        for j in tokens:
            word = lmtzr.lemmatize(j[0], get_pos(j[1]))
            if word in stopwords:
                continue
            if word in document[doc_count].keys():
                document[doc_count][word] += 1
            else:
                document[doc_count][word] = 1
print(sorted(document[0].items(), key = lambda d:d[1], reverse = True))

"""
result = dict()
for i in document:
    for j in i.keys():
        if j in result.keys():
            result[j] += i[j]
        else:
            result[j] = i[j]

print(sorted(result.items(), key = lambda d:d[1], reverse = True))
"""
print("finish")


#print(nltk.corpus.wordnet.ADV)

