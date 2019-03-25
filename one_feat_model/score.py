import csv
import json
import time
from textblob import TextBlob
from features import build_vocab
from google.cloud import translate
from spellchecker import SpellChecker


neu_features = "neu_features.txt"
neu_feature_file = open(neu_features, "r")

neg_features = "neg_features.txt"
neg_feature_file = open(neg_features, "r")

pos_features = "pos_features.txt"
pos_feature_file = open(pos_features, "r")

neu_set = set()
neu_set_c = set()

neg_set = set()
neg_set_c = set()

pos_set = set()
pos_set_c = set()
pos_set_cc = set()

for neu_word in neu_feature_file:

    neu_word = neu_word.lower()
    neu_set.add(neu_word)
    neu_set_c.add(neu_word)

for neg_word in neg_feature_file:

    neg_word = neg_word.lower()
    neg_set.add(neg_word)
    neg_set_c.add(neg_word)

for pos_word in pos_feature_file:

    pos_word = pos_word.lower()
    pos_set.add(pos_word)
    pos_set_c.add(pos_word)
    pos_set_cc.add(pos_word)


pos_set.difference_update(neg_set)
pos_set.difference_update(neu_set)

neg_set.difference_update(pos_set_c)
neg_set.difference_update(neu_set)

neu_set.difference_update(neg_set_c)
neu_set.difference_update(pos_set_cc)

pos_set.discard('EMOPOS')
pos_set.discard('EMONEG')
pos_set.discard('EMONEU')

neg_set.discard('EMOPOS')
neg_set.discard('EMONEG')
neg_set.discard('EMONEU')

neu_set.discard('EMOPOS')
neu_set.discard('EMONEG')
neu_set.discard('EMONEU')

pos_set.add('EMOPOS')
neg_set.add('EMONEG')
neu_set.add('EMONEU')

h2h_list = []
h2e_list = []
row = []
i = 1
flag = 0
found = 0
not_found = 1

with open('h2e.csv', 'r') as f:
    
  reader = csv.reader(f)
  h2e_list = list(reader)

with open('h2h.txt', 'r') as h2h:
    
    for line in h2h:

        word = line.split()
        h2h_list.append(word)

print("Training the Model, Sit back and relax........")

with open('train.json') as json_data:

    d = json.load(json_data)

column_headers = ['score', 'value']

with open('data.csv', 'w') as csvFile:

    writer = csv.writer(csvFile)
    writer.writerow(column_headers)

    for each in d:

        print("..", i, "..")

        sentence = each["text"]
        senti_value = each["sentiment"]
        word_id = each["lang_tagged_text"]
        word_id = word_id.replace(" ", "")
        word_id = word_id.lower()
        tokens = build_vocab(sentence)

        sent_score = 0
            
        for token in tokens:
                    
            if token in pos_set:

                sent_score += 30
                continue
                        
            if token in neu_set:

                sent_score += 20
                continue

            if token in neg_set:

                sent_score += 10
                continue
                    
            else:

                find_pos = token.find('emopos')
                find_neu = token.find('emoneu')
                find_neg = token.find('emoneg')

                if(find_pos == -1 and find_neg == -1 and find_neu == -1):

                    start = word_id.find(token)

                    if(start == -1):
                        continue

                    else:

                        end = start + len(token)
                        check = word_id[end+1]

                        if(check == "e"):

                            spell = SpellChecker()

                            if(spell.known(token)):

                                testimonial = TextBlob(token)
                                polarity = testimonial.sentiment.polarity

                                if(polarity >= .2):
                                    sent_score += 30

                                elif(polarity > -.2 and polarity < .2):
                                    sent_score += 20

                                else:
                                    sent_score += 10

                            else:

                                new_token = spell.correction(token)
                                new_token = new_token.lower()

                                testimonial = TextBlob(new_token)
                                polarity = testimonial.sentiment.polarity

                                if(polarity >= .2):
                                    sent_score += 30

                                elif(polarity > -.2 and polarity < .2):
                                    sent_score += 20

                                else:
                                    sent_score += 10

                        elif(check == 'h'):

                            j = 0

                            for ii in h2h_list:

                                if(j < len(h2h_list) - 1):

                                    key = h2h_list[j][0]
                                    val = h2h_list[j][1]

                                    j += 1

                                    if(token == key):

                                        flag = 1

                                        translate_tok = val

                                        kk = 0

                                        for sss in h2e_list:

                                            if(kk < len(h2e_list)):

                                                eng_tok = h2e_list[kk][0]
                                                hin_tok = h2e_list[kk][1]

                                                kk += 1

                                                if(translate_tok == hin_tok):

                                                    found = 1

                                                    found_eng_tok = eng_tok

                                                    testimonial = TextBlob(found_eng_tok)
                                                    polarity = testimonial.sentiment.polarity

                                                    if(polarity >= .2):
                                                        sent_score += 30

                                                    elif(polarity > -.2 and polarity < .2):
                                                        sent_score += 20

                                                    else:
                                                        sent_score += 10

                                        if(found != 1):
                                        
                                            translate_client = translate.Client()
                                            translation = translate_client.translate(translate_tok, source_language='hi')
                                            converted_tok = translation['translatedText']

                                            testimonial = TextBlob(converted_tok)
                                            polarity = testimonial.sentiment.polarity

                                            if(polarity >= .2):
                                                sent_score += 30
                                    
                                            elif(polarity > -.2 and polarity < .2):
                                                sent_score += 20

                                            else:
                                                sent_score += 10


                            if(flag != 1):

                                translate_client = translate.Client()
                                target = 'hi'
                                translation = translate_client.translate(token, target_language=target, source_language='en')

                                converted_tok = translation['translatedText']

                                k = 0
                                
                                for ss in h2e_list:

                                    if(k < len(h2e_list)):

                                        eng = h2e_list[k][0]
                                        hin = h2e_list[k][1]
                                        k += 1
                                        
                                        if(converted_tok == hin):

                                            not_found = 0

                                            converted_tok = eng
                                            testimonial = TextBlob(converted_tok)
                                            polarity = testimonial.sentiment.polarity

                                            if(polarity >= .2):
                                                sent_score += 30

                                            elif(polarity > -.2 and polarity < .2):
                                                sent_score += 20

                                            else:
                                                sent_score += 10


                                if(not_found != 0):

                                    translate_client = translate.Client()
                                    target = 'en'
                                    translation = translate_client.translate(token, target_language=target, source_language='hi')

                                    f_eng_tok = translation['translatedText']

                                    testimonial = TextBlob(f_eng_tok)
                                    polarity = testimonial.sentiment.polarity

                                    if(polarity >= .2):
                                        sent_score += 30

                                    elif(polarity > -.2 and polarity < .2):
                                        sent_score += 20

                                    else:
                                        sent_score += 10


                elif(find_pos > 0):
                    sent_score += 30
                    continue

                elif(find_neu > 0):
                    sent_score += 20
                    continue
                
                else:
                    sent_score += 10
                    continue
                    
 
        row.append(sent_score)
        row.append(senti_value)
                
        writer.writerow(row)
        row = []
        i += 1

print("Done! Now Run accuracy.py")