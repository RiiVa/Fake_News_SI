import math
import sys,os,re
import json, codecs
import numpy as np
import csv
file=open('fakenews.csv','w',newline='')
spamreader=csv.writer(file)
a=csv
def collector(directory):
    for root,_,fds in os.walk(directory):
        # Para filtrar las expresiones regulares
        r=re.compile('(.)+(.txt)$')
        rfake=re.compile('(.)+fake$')
        for t in (filter(r.match,fds)):
            # Para obtener el dominio completo concateno el dominio actual con el nombre del archivo
            dict_file={}
            name=os.path.join(root,t)
            dict_file['name']=os.path.basename(name)
            dict_file['size']=round(os.path.getsize(name) / 1024, 3)
            yield (name,dict_file,0 if rfake.match(root) else 1)

class GetText():
    def __init__(self):
        pass
    def getText(self,directory):
        return self.getTextOfTxt(directory)
    def getTextOfTxt(self,directory):
        fd=open(directory,'r')
        return fd.read()
def GetNews():
    direction=os.path.join(os.getcwd(),"fakeNewsBigDatasets")
    g=GetText()
    labels=[]
    news=[]
    for direction,_,n in collector(direction):
        try:
            news.append(g.getText(direction))
            labels.append(n)
        except:
            pass
    return labels,news
def Vectorize(labels,texts,max_words):
    
    from keras.preprocessing.text import Tokenizer
    from keras.preprocessing.text import tokenizer_from_json
    from keras.preprocessing.sequence import pad_sequences
    
    maxlen = 100 
    training_samples = 200
    validation_samples = 10000

    
    # tokenizamos los textos
    tokenizer = Tokenizer(num_words = max_words)
    tokenizer.fit_on_texts(texts)
    # convierte los strings en una lista de los indices of tokens 
    sequences = tokenizer.texts_to_sequences(texts)

    # diccionario de los tokens con sus indices
    word_index = tokenizer.word_index
    # print('Found unique tokens')

    # esto conviere una lista en una matrix 2D
    data = pad_sequences(sequences)
    labels = np.asarray(labels)
    # print('Shape of data tensor:', data.shape)
    # print('Shape of label:',labels.shape)

    # hago una permutacion random de los features
    indices = np.arange(data.shape[0])
    np.random.shuffle(indices)
    data = data[indices]
    labels = labels[indices]
    print(labels)
    return data,labels

def TextMetadata(news):
    from text_metadata import Metadata
    m=Metadata()
    text_metadata=np.asarray([m(n) for n in news])
    # print(news)
    if os.path.exists("mean.json"):
        # print("entro aqui")
        with codecs.open("mean.json",'r',encoding='utf-8') as f:
	        mean_denom = json.loads(f.read())
    if os.path.exists("std.json"):
        # print("entro aqui")
        with codecs.open("std.json",'r',encoding='utf-8') as f:
	        std_denom = json.loads(f.read())
    print(mean_denom)
    print(std_denom)
    text_metadata-= mean_denom
    # print(text_metadata.std(axis = 0))
    text_metadata /= std_denom
    print(text_metadata)
    return text_metadata

def Vectorize2(news_list , json_string, max_words = 100):
    
    from keras.preprocessing.text import tokenizer_from_json
    from keras.preprocessing.sequence import pad_sequences
    
    maxlen = 100 
    training_samples = 200
    validation_samples = 10000

    
    # tokenizamos los textos
    tokenizer = tokenizer_from_json(json_string)
    
    # convierte los strings en una lista de los indices of tokens 
    sequences = tokenizer.texts_to_sequences(news_list)
    # print(len(sequences[0]))
    # diccionario de los tokens con sus indices
    word_index = tokenizer.word_index
    # print(len(word_index.keys()))
    # print('Found unique tokens')

    # esto conviere una lista en una matrix 2D
    data = pad_sequences(sequences, maxlen=1494)
    
    # print('Shape of data tensor:', data.shape)
    # print('Shape of label:',labels.shape)

    # hago una permutacion random de los features
    # indices = np.arange(data.shape[0])
    # np.random.shuffle(indices)
    # data = data[indices]
    # labels = labels[indices]
    # print(labels)
    return data

# labels,news=GetNews()
# max_words = 100
# data,labels=Vectorize(labels,news,max_words)
# text_metadata=TextMetadata(news)

