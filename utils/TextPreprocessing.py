import nltk
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


def tokenization(text):
    list_token = word_tokenize(text.lower())
    return list_token

def stemming(list_token):
    pst = PorterStemmer()
    list_stemming = list()
    for x in list_token:
        list_stemming.append(pst.stem(x))

    return list_stemming

def lemmatization(list_token):
    lemmatizer = WordNetLemmatizer() 
    list_lemmatization = list()
    for x in list_token:
        list_lemmatization.append(lemmatizer.lemmatize(x))
    
    return list_lemmatization


def stop_words(list_token):
    stopwords_dict = set(stopwords.words('english'))
    result_stopwords = [x for x in list_token if x not in stopwords_dict]
    return result_stopwords