import re
import json
import nltk
import string
import collections
from string import punctuation
from collections import Counter
from nltk.corpus import stopwords
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

def vectorize(vec_tok):

    vect = CountVectorizer().fit(vec_tok)
    vect.get_feature_names()[::2000]

def clean_text(preprocess_text, vocab):

    try:  
        # split into tokens by white space
        tokens = preprocess_text.split()  
        # filter out tokens not in vocab
        preprocess_tokens = [w for w in tokens if w in vocab]
        preprocess_tokens = ' '.join(preprocess_tokens)
        #train = vectorize(preprocess_tokens)

        return preprocess_tokens

    except Exception as inst:

        print inst
        pass

def load_vocab(filename):

	# open the file as read only
	file = open("vocab.txt", "r")
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text

vocab_file = 'vocab.txt'
vocab = load_vocab(vocab_file)

with open('codemix_train.json') as json_data:
    d = json.load(json_data)

for text in d:
    text = text["text"]
    tokens = clean_text(text, vocab)

print "----------------------------------------analyzing testdata------------------------------------"

with open('codemix_Test.json') as json_data_test:
    e = json.load(json_data_test)

for text in e:
    text = text["text"]
    test_data = clean_text(text, vocab)


# classifier = LogisticRegression()
# classifier.fit(train, sent_vec)

