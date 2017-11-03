'''
Created on 5 de mai de 2017

@author: Alan James
'''
from _operator import itemgetter

import nltk
from nltk.classify.naivebayes import NaiveBayesClassifier

from application.naive_bayes_custom import _LEXICON, __TRAIN_SET__
from application.naive_bayes_custom.pre_processing_text import PreProcessingText
from application.naive_bayes_custom.processing_text import ProcessingText


pt = ProcessingText()
prePt = PreProcessingText()

class NaiveBayesCustom(object):
    
    _classifier = None
    _featurized_test_sentence = None
    
    def __init__(self):
        pass
   
    def preProcessingTrain(self):
        preTrain = prePt.applyRemovalStopwordsPreTrainSet()
        #print("Apply stopwords", preTrain)
        #preTrain = pt.cleanListWords(preTrain)
        #print("Clean: ", preTrain)
        preTrain = pt.applyStemmersByList(preTrain)
        #print("Apply stemmers", preTrain)
        return set(preTrain)
        
    def preProcessingTest(self, text):
        pass
    
    def extractFeature(self, document):
        return {word.lower(): (word in set(document)) for word in _LEXICON}
    '''
    def trainCustom(self, trainSet):
        self._test_set = [({word: (word in pt.applyTokenizer(x[0])) for word in trainSet}, x[1]) for x in __TRAIN_SET__]
        print("> Test Set: ", self._test_set)
        self._training_set = apply_features(self.extractFeature, self._test_set)
        self._classifier = NaiveBayesClassifier.train(self._training_set)
        print("> Tragining Set: ", self._training_set)
    '''
   
    def train(self):
        
        self._test_set = [({word: (word in pt.applyTokenizer(x[0])) for word in _LEXICON}, x[1]) for x in __TRAIN_SET__]
        #print("> Test Set: ", self._test_set)
        
        #self._training_set = apply_features(self.extractFeature, self._test_set)
        self._classifier = NaiveBayesClassifier.train(self._test_set)
        #print("> Training Set: ", self._training_set)
        
    def trainCustom(self, trainSet):
        #print("\n> Train set custom", trainSet)
        self._test_set = [({word: (word in pt.applyTokenizer(x[0])) for word in trainSet}, x[1]) for x in __TRAIN_SET__]
        #print("> Test Set: ", self._test_set)
        #self._training_set = apply_features(self.extractFeature, self._test_set)
        self._classifier = NaiveBayesClassifier.train(self._test_set)
        #print("> Training Set: ", self._training_set)
        
    def test(self, testTrain):
        self._featurized_test_sentence = {word.lower(): (word in testTrain) for word in _LEXICON} #pt.cleanText(pt.applyTokenizer(testTrain))
        #print("> Featurized test sentence: ", self._featurized_test_sentence)
        return self._featurized_test_sentence
    
    def getAccuracy(self):
        return nltk.classify.accuracy(self._classifier, self._test_set) #self._training_set(errado), self._test_set (atualf)
    
    def getClassification(self):
        return self._classifier.classify(self._featurized_test_sentence)
    
    def getProbabilityAllClasses(self):
        """
        return probabilities for all 'classes'
        """
        # Probability dicionary class 
        dictProbs = self._classifier.prob_classify(self._featurized_test_sentence)
        probLabels = []
        for label in dictProbs.samples():
            probLabels.append((label, "{0:.4f}".format(dictProbs.prob(label))))
            probLabels.sort(key=itemgetter(0)) #(key=lambda tup: tup[0])
        return probLabels       
