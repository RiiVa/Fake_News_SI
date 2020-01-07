# from nltk import FreqDist
# texts=["I I love little girl make me feel so good","Ohh you touch me my ta la la ummm I ding ding dong"]
from nltk import sent_tokenize
from nltk import word_tokenize
# from recollect import news
import numpy as np
import re
from functools import reduce
# print()
class Metadata(object):
    def __init__(self):
        pass
    def __call__(self,text):
        self.sent_tokenize_text=[word_tokenize(s) for s in sent_tokenize(text)]
        # print(text)
        return [self.__ave_of_senteces_l(),self.__number_of_words(), self.__question_mark(),self.__exclamation_mark(),self.__negation_in_the_news(),self.__lexical_diversity(),self.__FPP()]
    # def __number_of_sentences(self,text):
    #     return len(self.sent_tokenize_text)
    def __ave_of_senteces_l(self):
        # print(list(map(len,self.sent_tokenize_text)))
        return np.mean(np.asarray(list(map(len,self.sent_tokenize_text))))
    def __number_of_words(self):
        return sum(list(map(len,self.sent_tokenize_text)))
    def __question_mark(self):
        return sum([ sum([ 1 if w=='?' or w=='¿' else 0 for w in s]) for s in self.sent_tokenize_text])
    def __exclamation_mark(self):
        return sum([ sum([ 1 if w=='!' or w=='¡' else 0 for w in s]) for s in self.sent_tokenize_text])
    def __negation_in_the_news(self):
        return sum([ sum([ 1 if (w=='No' or w=='no' or w=='Not' or w=='not') else 0 for w in s]) for s in self.sent_tokenize_text])
    def __lexical_diversity(self):
        words=reduce( lambda x,y:x+y, [[ w.casefold() for w in s if w.isalnum()] for s in self.sent_tokenize_text ])
        wordsDif=set(words)
        return len(wordsDif)/len(words)
    def __FPP(self):
        return sum([ sum([ 1 if w=='we' or w=='We' or w=='I' else 0 for w in s]) for s in self.sent_tokenize_text])



# w=[word_tokenize(s) for s in sent_tokenize("I love you. But not")]
# for new in news[:3]:
#     print(m(new))