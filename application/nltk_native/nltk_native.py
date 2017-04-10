#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Mar 31, 2017

@author: Alan James
'''

from _datetime import timedelta
import csv
from datetime import datetime

from nltk import NaiveBayesClassifier
import nltk
from nltk.classify import apply_features
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from nltk.stem.rslp import RSLPStemmer
from _operator import itemgetter


_TEXT       = "quero muito nadar hoje"
_FILECSV    = "C:\\Users\\Alan James\\Documents\\Development\\work-space\\bonito-turista-atrativos-train-2.csv"
_LANGUAGE   = 'portuguese'

START_TIME = datetime.now().strftime('%H:%M:%S')
HOUR = int(START_TIME[:2])
MIN  = int(START_TIME[3:5])
SEC  = int(START_TIME[6:])

def readFileCSV(filePath):
    training_set = []
    with open(filePath, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            training_set.append((row[0], row[1]))
    return training_set

__FILE_TRAIN = readFileCSV(_FILECSV)
_ALL_WORDS   = set(word.lower() for passage in __FILE_TRAIN for word in word_tokenize(passage[0], language=_LANGUAGE))

def isPunct(word):
    return len(word) == 1 and word in string.punctuation

def isDigits(word):
    return word in string.digits

def extractFeature(document):
    return {'contains(%s)'% word.lower(): (word in set(document)) for word in _ALL_WORDS}

def treatTokens():
    #print(RSLPStemmer().stem('Viajando'))
    
    print("Depois: ", _ALL_WORDS)
    global _ALL_WORDS
    stopWords = set(stopwords.words(_LANGUAGE))
    allWords = list(_ALL_WORDS)
    for word in allWords:
        if word in stopWords or isPunct(word) or isDigits(word):
            #print("Excluido > ", word)
            _ALL_WORDS.remove(word)
        else:
            l = list(_ALL_WORDS)
            l[l.index(word)] = RSLPStemmer().stem(word)
            _ALL_WORDS = set(l)
    print("Stemmers: ", _ALL_WORDS)  

def train():
    all_words = set(word.lower() for passage in __FILE_TRAIN for word in word_tokenize(passage[0], language=_LANGUAGE))

    test_set = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in __FILE_TRAIN]
    
    classifier = NaiveBayesClassifier.train(test_set)
    
    featurized_test_sentence = {word.lower(): (word in word_tokenize(_TEXT.lower())) for word in all_words}
    
    print("Classification: %s" %classifier.classify(featurized_test_sentence), "\nAccuracy: %.4f" %nltk.classify.accuracy(classifier, test_set))
    
    # Probabilidade por 'labels'
    probs = classifier.prob_classify(featurized_test_sentence)
    print("\nProbability\n---\nPOS: %.4f\nNEG: %.4f" %(probs.prob('POS'), probs.prob('NEG')))
    #for label in probs.samples():
    #    print("%s: %f" % (label, probs.prob(label)))

def getProbabilitiesAllLabels(dictinaryProbs):
    probLabels = []
    for label in dictinaryProbs.samples():
        probLabels.append((label, dictinaryProbs.prob(label)))
    return probLabels.sort(reverse=True)

def trainInMemory():
    print("TEST IN MEMORY")
    
    test_set = [({word: (word in word_tokenize(x[0])) for word in _ALL_WORDS}, x[1]) for x in __FILE_TRAIN]
    training_set = apply_features(extractFeature, test_set)
    classifier = NaiveBayesClassifier.train(training_set)
    
    featurized_test_sentence = {word.lower(): (word in word_tokenize(_TEXT.lower(), language=_LANGUAGE)) for word in _ALL_WORDS}
    
    print("Classification: %s \nAccuracy: %.4f \n" %(classifier.classify(featurized_test_sentence), nltk.classify.accuracy(classifier, test_set)))
    
    dictProbs = classifier.prob_classify(featurized_test_sentence)
    
    #probLabels = getProbabilitiesAllLabels(dictProbs) ARRUMAR
    probLabels = []
    for label in dictProbs.samples():
        probLabels.append((label, dictProbs.prob(label)))
    probLabels.sort(key=itemgetter(0)) #(key=lambda tup: tup[0])
    print(probLabels)
    for content in probLabels:
        print("%.5f\t- %s" %(content[1], content[0]))
    
def finalTest():
    FINAL_HOUR =  datetime.now()
    RUN_TIME = FINAL_HOUR - timedelta(seconds=SEC, minutes=MIN, hours=HOUR)
    print("\n---\nTime inicial: %s\nTime Final: \t%s\nRun Time: \t%s" %(START_TIME, FINAL_HOUR.strftime('%H:%M:%S'), RUN_TIME.strftime('%H:%M:%S')))
    print('\n\n## End Test ##\n---')

if __name__ == '__main__':
    #trainInMemory()
    #finalTest()
    #print("\n\n===============\n\n")
    treatTokens()
    trainInMemory()
    #train()
    finalTest()