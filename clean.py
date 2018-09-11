import string
import json
import re
import collections
import nltk
import string
from gensim.models import Word2Vec
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from collections import Counter
 

# save list to file
def save_list(tokens, filename):
    # convert tokens to a single blob of text
    data = '\n'.join(tokens) + "\n"
    # open file
    file = open(filename,'a')
    # write text
    file.write(data)
    # close file
    file.close()



def preprocess_text(preprocess_text):
    # Remove punctuation
    exclude = set(string.punctuation)
    preprocess_text = ''.join(ch for ch in preprocess_text if ch not in exclude)                          #
    # preprocess_text = preprocess_text.strip('\'"?!,.():;')
    # Convert more than 2 letter repetitions to 2 letter
    # funnnnny --> funny
    preprocess_text = re.sub(r'(.)\1+', r'\1\1', preprocess_text)
    # Remove - & '
    preprocess_text = re.sub(r'(-|\')', '', preprocess_text)
    # Replaces #hashtag with hashtag
    preprocess_text = re.sub(r'#(\S+)', r' \1 ', preprocess_text)
    # Replace 2+ dots with space
    preprocess_text = re.sub(r'\.{2,}', ' ', preprocess_text)
    # Strip space, " and ' from text
    preprocess_text = preprocess_text.strip(' "\'')
    # Replace @handle with the word USER_MENTION
    preprocess_text = re.sub(r'@[\S]+', 'USER_MENTION', preprocess_text)
    # Replaces URLs with the word URL
    preprocess_text = re.sub(r'((www\.[\S]+)|(https?://[\S]+))', ' URL ', preprocess_text)
    # Replace multiple spaces with a single space
    preprocess_text = re.sub(r'\s+', ' ', preprocess_text)
    # removing certain words
    preprocess_text = re.sub(r'http', '', preprocess_text)
    preprocess_text = re.sub(r'url', '', preprocess_text)
    preprocess_text = re.sub(r'ensuffix', '', preprocess_text)

    return preprocess_text



def handle_emojis(text):
    # Smile -- :), : ), :-), (:, ( :, (-:, :')
    text = re.sub(r'(:\)|:-\)|\(\s:|\(-:|:\'\))', ' EMO_POS ', text)
    # Laugh -- :D, : D, :-D, xD, x-D, XD, X-D, :-d, :d
    text = re.sub(r'(:D|:-D|x-D|X-D|:-d|:d)', ' EMO_POS ', text)
    # Love -- <3, :*
    text = re.sub(r'(<3|:\*)', ' EMO_POS ', text)
    # Wink -- ;-), ;), ;-D, ;D, (;,  (-;
    text = re.sub(r'(;-\)|;-D|\(-;)', ' EMO_POS ', text)
    # Sad -- :-(, : (, :(, ):, )-:, -_-
    text = re.sub(r'(:\(|:-\(|\)\s:|\)-:|-_-)', ' EMO_NEG ', text)
    # Cry -- :,(, :'(, :"(
    text = re.sub(r'(:,\(|:\'\(|:"\()', ' EMO_NEG ', text)
    # Shout -- :@
    text = re.sub(r'(:\@)', ' EMO_NEG ' , text)
    # coded emoji
    text = re.sub(r'(\ud83d\ude08)', ' EMO_NEG ' , text)

    return text


def build_vocab(text):
    try:
        # split into tokens by white space
        # tokens = text.split()
        lower_text = text.lower() 
        # turn a doc into clean tokens
        processed_text = handle_emojis(lower_text)
        final_text = preprocess_text(processed_text)
        print final_text
        #tokenize
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(final_text)
        # remove remaining tokens that are not alphabetic
        tokens = [word for word in tokens if word.isalpha()]
        # filter out stop words
        stop_words = set(stopwords.words('english'))
        tokens = [w for w in tokens if not w in stop_words]
        # filter out short tokens
        # tokens = [word for word in tokens if len(word) > 1]

        # write to txt file
        save_list(tokens, 'vocab.txt')

    except Exception as inst:
        print inst
        pass
 
# load the document

with open('HN-EN_train.json') as json_data:
    d = json.load(json_data)

for text in d:
    text = text["text"]
    tokens = build_vocab(text)


