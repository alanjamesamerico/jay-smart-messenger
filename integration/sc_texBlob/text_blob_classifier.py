'''
Created on 24 de nov de 2016

@author: alan.james
'''

from _io import open
from builtins import sorted
from textblob.classifiers import NaiveBayesClassifier
import operator

def train_data(_FILEPATH):   
    """
    Função que faz treinamento apenas com arquivos '.csv'
    @param Um arquivo de extensão .csv: 
    """
    with open(_FILEPATH, 'r') as fp:
        trained_classification = NaiveBayesClassifier(fp, format='csv')
    return trained_classification
    

def get_all_prob_labels(classifier, text):
    prob_labels = {}
    prob_dist = classifier.prob_classify(text)
    for label in classifier.labels():
        prob_labels[label] = (round(prob_dist.prob(label), 5))
    dic_labels = sorted(prob_labels.items(), key=operator.itemgetter(1), reverse=True)
    return dic_labels