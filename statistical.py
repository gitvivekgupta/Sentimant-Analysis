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



def coded_emojis(processed_text):

    try:



#----------------------------------------------------------------------------------------------
#--------------\ud83d\ude------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------


        happy_emoji = re.compile(u"(\ud83d[\ude00-\ude09])" "+", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d[\ude17-\ude19])" "+", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d[\ude42-\ude43])" "+", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d[\ude47-\ude49])" "+", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d[\ude38-\ude39])" "+", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
    
    
        happy_emoji = re.compile(u"(\ud83d\ude0a)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\ude0b)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\ude0c)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\ude0d)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\ude0e)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
    
    
        happy_emoji = re.compile(u"(\ud83d\ude1a)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\ude1b)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\ude1c)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\ude1d)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
    
    
        happy_emoji = re.compile(u"(\ud83d\ude2c)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
    
        happy_emoji = re.compile(u"(\ud83d\ude3a)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\ude3b)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\ude3c)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\ude3d)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
    
    
        happy_emoji = re.compile(u"(\ud83d\ude4a)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\ude4b)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\ude4c)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\ude4e)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
    
    
        happy_emoji = re.compile(u"(\ud83d\ude47\u200d\u2640)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\ude46\u200d\u2642)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\ude4b\u200d\u2642)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\ude4e\u200d\u2642)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udeb4\u200d\u2640)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udeb5\u200d\u2640)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udeb5\u200d\u2640)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)


#----------------

        sad_emoji = re.compile(u"(\ud83d[\ude13-\ude16])" "+", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d[\ude10-\ude12])" "+", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d[\ude20-\ude37])" "+", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d[\ude40-\ude41])" "+", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d[\ude44-\ude45])" "+", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d\ude4d\u200d\u2642)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d\ude0f)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d\ude1e)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d\ude1f)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d\ude2b)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d\ude2f)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d\ude2e)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d\ude3f)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d\ude2d)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d\ude2a)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d\ude3e)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)




#--------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
#--------------\ud83e\udd----------




        happy_emoji = re.compile(u"(\ud83e[\udd16-\udd19])" "+", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83e[\udd20-\udd21])" "+", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83e[\udd23-\udd24])" "+", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83e[\udd33-\udd36])" "+", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83e[\udd42-\udd43])" "+", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
      
    
        happy_emoji = re.compile(u"(\ud83e\udd11)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83e\udd13)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83e\udd30)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83e\udd81)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83e\udd84)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
    
    
        happy_emoji = re.compile(u"(\ud83e\udd8b)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
    
    
        happy_emoji = re.compile(u"(\ud83e\udd1a)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83e\udd1d)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83e\udd1e)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)



#--------


        sad_emoji = re.compile(u"(\ud83e[\udd14-\udd15])" "+", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83e[\udd47-\udd49])" "+", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83e[\udd24-\udd25])" "+", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83e[\udd90-\udd91])" "+", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83e[\udd87-\udd89])" "+", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83e\udd26\u200d\u2640)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83e\udd26\u200d\u2642)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83e\udd37\u200d\u2640)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83e\udd37\u200d\u2642)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83e\udd10)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83e\udd22)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83e\udd27)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83e\udd12)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83e\udd1b)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83e\udd1c)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83e\udd8a)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83e\udd8c)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83e\udd8e)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83e\udd82)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83e\udd80)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)





#--------------------------------------------------------------------------------------------------------------------------------------
#--------------\u263a\----
#-------------------------------------------------------------------------------------------------------------------------------------
 
        happy_emoji = re.compile(u"(\u263a\ufe0f)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)

#--------------------------------------------------------------------------------------------------------------------------------------
#--------------\u2615\----
#-------------------------------------------------------------------------------------------------------------------------------------
 
        happy_emoji = re.compile(u"(\u2615\ufe0f)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)

#-----------------------------------------
#--------------\u2639\----

        sad_emoji = re.compile(u"(\u2639\ufe0f)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)



#----------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------
#--------------\ud83d\udc---------------------------------------------------------------------------------------------------



        happy_emoji = re.compile(u"(\ud83d[\udc83-\udc85])" "+", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d[\udc91-\udc93])" "+", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d[\udc95-\udc99])" "+", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d[\udc70-\udc71])" "+", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc51)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc44)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc76)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc78)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)




        happy_emoji = re.compile(u"(\ud83d\udc6f\u200d\u2642)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc69\u200d\u2764\ufe0f\u200d\ud83d\udc69)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc68\u200d\u2764\ufe0f\u200d\ud83d\udc68)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc69\u200d\u2764\ufe0f\u200d\ud83d\udc8b\u200d\ud83d\udc69)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text) 
    
        happy_emoji = re.compile(u"(\ud83d\udc68\u200d\u2764\ufe0f\u200d\ud83d\udc8b\u200d\ud83d\udc68)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text) 
    
        happy_emoji = re.compile(u"(\ud83d\udc68\u200d\ud83d\udc69\u200d\ud83d\udc67)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc68\u200d\ud83d\udc69\u200d\ud83d\udc67\u200d\ud83d\udc66)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc68\u200d\ud83d\udc69\u200d\ud83d\udc66\u200d\ud83d\udc66)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc68\u200d\ud83d\udc69\u200d\ud83d\udc67\u200d\ud83d\udc67)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc69\u200d\ud83d\udc69\u200d\ud83d\udc66)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc69\u200d\ud83d\udc69\u200d\ud83d\udc67)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc69\u200d\ud83d\udc69\u200d\ud83d\udc67\u200d\ud83d\udc66)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc69\u200d\ud83d\udc69\u200d\ud83d\udc66\u200d\ud83d\udc66)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc69\u200d\ud83d\udc69\u200d\ud83d\udc66\u200d\ud83d\udc66)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc69\u200d\ud83d\udc69\u200d\ud83d\udc67\u200d\ud83d\udc67)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc68\u200d\ud83d\udc68\u200d\ud83d\udc66)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc68\u200d\ud83d\udc68\u200d\ud83d\udc67)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc68\u200d\ud83d\udc68\u200d\ud83d\udc67\u200d\ud83d\udc66)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc68\u200d\ud83d\udc68\u200d\ud83d\udc66\u200d\ud83d\udc66)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc68\u200d\ud83d\udc68\u200d\ud83d\udc67\u200d\ud83d\udc67)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc69\u200d\ud83d\udc67\u200d\ud83d\udc66)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc69\u200d\ud83d\udc66\u200d\ud83d\udc66)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc69\u200d\ud83d\udc67\u200d\ud83d\udc67)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc68\u200d\ud83d\udc67\u200d\ud83d\udc66)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc68\u200d\ud83d\udc66\u200d\ud83d\udc66)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc68\u200d\ud83d\udc67\u200d\ud83d\udc67)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc68\u200d\ud83d\udc67\u200d\ud83d\udc67)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc71\u200d\u2640)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc69\u200d\ud83d\udc66)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc69\u200d\ud83d\udc67)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc68\u200d\ud83d\udc66)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc68\u200d\ud83d\udc67)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)



        happy_emoji = re.compile(u"(\ud83d\udc6a)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc6b)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc6d)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc6f)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)




        happy_emoji = re.compile(u"(\ud83d\udc9f)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc9d)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc9e)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)




        happy_emoji = re.compile(u"(\ud83d\udc4f)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc4d)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc4b)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc4c)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)





        happy_emoji = re.compile(u"(\ud83d\udc8d)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc8b)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc8f)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc8e)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
    
    
        happy_emoji = re.compile(u"(\ud83d\udc9c)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc9a)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udc9b)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
    
    
        happy_emoji = re.compile(u"(\ud83d\udcab)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udcaf)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83d\udcaa)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
    
    
        happy_emoji = re.compile(u"(\ud83d\udc7c)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)


#------------------

        sad_emoji = re.compile(u"(\ud83d[\udc79-\udc80])" "+", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d[\udc36-\udc37])" "+", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d\udc45)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d\udc31)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d\udc94)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d\udc89)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
        
        sad_emoji = re.compile(u"(\ud83d\udc16)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
    
    
        sad_emoji = re.compile(u"(\ud83d\udc7a)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d\udc7b)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d\udc7d)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d\udc7e)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
    
    
    
        sad_emoji = re.compile(u"(\ud83d\udc4e)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d\udc4a)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
    
    
        sad_emoji = re.compile(u"(\ud83d\udc2d)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d\udc8a)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
    
    
    
        sad_emoji = re.compile(u"(\ud83d\udca2)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d\udca3)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d\udca6)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83d\udca9)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
    
    
        neutral_emoji = re.compile(u"(\ud83d\udc46)", flags=re.UNICODE)
        processed_text = neutral_emoji.sub(r' EMONEU ', processed_text)




#--------------------------------------------------------------------------------------------------------------------------------
#--------------\ud83c\udf------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------



        happy_emoji = re.compile(u"(\ud83c[\udf80-\udf82])" "+", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c[\udf83-\udf87])" "+", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c[\udf75-\udf79])" "+", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c[\udf96-\udf97])" "+", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c[\udf69-\udf70])" "+", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
    
    
    
    
    
        happy_emoji = re.compile(u"(\ud83c\udf08)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udf93)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udf32)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text) 
    
        happy_emoji = re.compile(u"(\ud83c\udf39)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text) 
    
        happy_emoji = re.compile(u"(\ud83c\udf89)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udf20)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udf05)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
    
    
    
    
        happy_emoji = re.compile(u"(\ud83c\udfcb\ufe0f\u200d\u2640\ufe0f)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udfcc\ufe0f\u200d\u2640\ufe0f)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udfc4\u200d\u2640)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udfca\u200d\u2640)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
    
    
    
    
    
    
    
    
        happy_emoji = re.compile(u"(\ud83c\udf7a)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udf7b)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udf7c)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udf7e)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udf7f)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
    
    
        happy_emoji = re.compile(u"(\ud83c\udfc2)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udfc4)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udfc5)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udfc6)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udfc7)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
    
    
    
    
    
        happy_emoji = re.compile(u"(\ud83c\udfca)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udfcb)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udfcc)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
    
    
    
    
    
    
    
    
        happy_emoji = re.compile(u"(\ud83c\udfa1)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udfa2)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udfa9)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
    
    
    
        happy_emoji = re.compile(u"(\ud83c\udfad)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udfae)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udfaf)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
    
    
    
    
        happy_emoji = re.compile(u"(\ud83c\udf8a)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udfe9)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udf1f)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text) 
    
        happy_emoji = re.compile(u"(\ud83c\udfb3)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udff5)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udfbf)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
    
    
    
    
        happy_emoji = re.compile(u"(\ud83c\udf6a)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udf6b)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udf6c)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udf6d)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udf6e)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)

#----------------------

        sad_emoji = re.compile(u"(\ud83c\udf35)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
    
    
    
        sad_emoji = re.compile(u"(\ud83c\udf2a)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83c\udf2b)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)
    
        sad_emoji = re.compile(u"(\ud83c\udf21)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)




#-----------------------------------------


        neutral_emoji = re.compile(u"(\ud83c\udffb)", flags=re.UNICODE)
        processed_text = neutral_emoji.sub(r' EMONEU ', processed_text)
    
        neutral_emoji = re.compile(u"(\ud83c\udffc)", flags=re.UNICODE)
        processed_text = neutral_emoji.sub(r' EMONEU ', processed_text)




#-----------------------------------------
#--------------\u2620\ufe0f----

        sad_emoji = re.compile(u"(\u2620\ufe0f)", flags=re.UNICODE)
        processed_text = sad_emoji.sub(r' EMONEG ', processed_text)

#-----------------------------------------
#--------------\u270a----

        happy_emoji = re.compile(u"(\u270a)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)

#-----------------------------------------
#--------------\\u270c\ufe0f----

        happy_emoji = re.compile(u"(\u270c\ufe0f)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)



#-----------------------------------------
#--------------\ud83c\udf----

        happy_emoji = re.compile(u"(\ud83c\udf89)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udf81)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)
    
        happy_emoji = re.compile(u"(\ud83c\udf8a)", flags=re.UNICODE)
        processed_text = happy_emoji.sub(r' EMOPOS ', processed_text)


        return processed_text


    except Exception:
        pass



def handle_emojis(text):

    try:
        # shock_emoji = re.compile("[" u"\ud83d\ude31" "]+", flags=re.UNICODE)
        # text = emoji_pattern.sub(r' EMONEG ', text)
        # Smile -- :), : ), :-), (:, ( :, (-:, :')
        text = re.sub(r'(:\)|:-\)|\(\s:|\(-:|:\'\))', ' EMOPOS ', text)
        # Laugh -- :D, : D, :-D, xD, x-D, XD, X-D, :-d, :d
        text = re.sub(r'(:D|:-D|x-D|X-D|:-d|:d)', ' EMOPOS ', text)
        # Love -- <3, :*
        text = re.sub(r'(<3|:\*)', ' EMOPOS ', text)
        # Wink -- ;-), ;), ;-D, ;D, (;,  (-;
        text = re.sub(r'(;-\)|;-D|\(-;)', ' EMOPOS ', text)
        # Sad -- :-(, : (, :(, ):, )-:, -_-
        text = re.sub(r'(:\(|:-\(|\)\s:|\)-:|-_-)', ' EMONEG ', text)
        # Cry -- :,(, :'(, :"(
        text = re.sub(r'(:,\(|:\'\(|:"\()', ' EMONEG ', text)
        # Shout -- :@
        text = re.sub(r'(:\@)', ' EMONEG ' , text)
        text = coded_emojis(text)
    
        return text

    except Exception:
        pass


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