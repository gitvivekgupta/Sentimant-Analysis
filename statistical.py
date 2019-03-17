import re
import json
import nltk
import string
import collections
from string import punctuation
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

from clean import preprocess_text
from clean import coded_emojis
from clean import build_vocab
from clean import handle_emojis



pos_dict = []
neu_dict = []
neg_dict = []
sentiments = []
true_count = 0
total_count = 0
accuracy = 0
emo_pos_count = 0
emo_neg_count = 0

neu_features = "neu_features.txt"
neg_features = "neg_features.txt"
pos_features = "pos_features.txt"

print("Predicting Accuracy............")

with open('eval.json') as json_data_test:
    e = json.load(json_data_test)

for text in e:

    try:

        text = text["text"]
        processed_text = handle_emojis(text)
        processed_text = re.sub(r'(.)\1+', r'\1\1', processed_text)
        processed_text = re.sub(r'#(\S+)', r' \1 ', processed_text)
        #deletes vowels along with g,y,n fromend ofword, leaves atleast a 2 char long stem,words like ‘aayenga’ do not completely vanish.
        processed_text = re.sub(r'(.{2,}?)([aeiougyn]+$)',r'\1', processed_text)
        lower_text = processed_text.lower()

        #tokenize
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(lower_text)
        # remove remaining tokens that are not alphabetic
        tokens = [word for word in tokens if word.isalpha()]
        # filter out stop words
        stop_words = set(stopwords.words('english'))
        tokens = [w for w in tokens if not w in stop_words]
        tokens = [word for word in tokens if len(word) > 1]   

        neu_feature_file = open(neu_features, "r")
        neg_feature_file = open(neg_features, "r")
        pos_feature_file = open(pos_features, "r")

        for token in tokens:

                no_pos = 0
                no_neu = 0

                if token == 'EMOPOS':
                        pos_dict.append(token)

                elif token == 'EMONEG':
                        neg_dict.append(token)
                
                elif token == 'EMONEU':
                        neu_dict.append(token)

                else:
                        
                        for pos_feature_word in pos_feature_file.readlines():
                                pos_feature_word = pos_feature_word.strip()
                                if token == pos_feature_word:
                                        pos_dict.append(token)
                                        no_pos = 1
                                        break
                                        
                        if no_pos == 0:
                                for neu_feature_word in neu_feature_file.readlines():
                                        neu_feature_word = neu_feature_word.strip()
                                        if token == neu_feature_word:
                                                neu_dict.append(token)
                                                no_neu = 1
                                                break
                        
                        if no_neu == 0:
                                for neg_feature_word in neg_feature_file.readlines():
                                        neg_feature_word = neg_feature_word.strip()
                                        if token == neg_feature_word:
                                                neg_dict.append(token)
                                                break

        pos_length = len(pos_dict)
        neu_length = len(neu_dict)
        neg_length = len(neg_dict)

        if pos_length > neg_length and neg_length > neu_length:
                sentiments.append(1)

        elif pos_length > neu_length and neu_length > neg_length:
                sentiments.append(1)

        elif neg_length > neu_length and neu_length < pos_length:
                sentiments.append(-1)

        elif neu_length > pos_length and pos_length > neg_length:
                sentiments.append(0)

        elif neu_length > neg_length and neg_length > pos_length:
                sentiments.append(0)

        elif neg_length > pos_length and pos_length > neu_length:
                sentiments.append(-1)

        elif neg_length > neu_length and neu_length > pos_length:
                sentiments.append(-1)

        elif neg_length > pos_length and pos_length > neu_length:
                sentiments.append(-1)

        elif pos_length == neu_length and pos_length > neg_length:
                sentiments.append(1)

        elif pos_length == neu_length and pos_length < neg_length:
                sentiments.append(-1)

        elif pos_length > neu_length and neu_length == neg_length:
                sentiments.append(1)

        elif pos_length < neu_length and neu_length == neg_length:
                sentiments.append(-1)

        elif pos_length == neg_length and neg_length < neu_length:
                sentiments.append(0)

        elif pos_length == neg_length and neg_length > neu_length:

                for emo_pos in pos_dict:
                        if emo_pos == 'EMOPOS':
                                emo_pos_count = emo_pos_count + 1

                for emo_neg in neg_dict:
                        if emo_neg == 'EMONEG':
                                emo_neg_count = emo_neg_count + 1
                
                if emo_pos_count > emo_neg_count:
                        sentiments.append(1)
                else:
                        sentiments.append(-1)
        else:
                sentiments.append(0)
                
        pos_dict.clear()
        neu_dict.clear()
        neg_dict.clear()

    except Exception:
        pass


for gained_sentiment in sentiments:
        for test_sentiment in e:
                original_sentiment = test_sentiment["sentiment"]

                if gained_sentiment == original_sentiment:
                        true_count = true_count + 1
                        break
                else:
                        break

        total_count = total_count + 1

accuracy = true_count/total_count*100
print("Gained Accuracy is", accuracy)
