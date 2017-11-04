'''
Created on 5 de mai de 2017

@author: Alan James
'''

from nltk.classify import accuracy
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
        #self._training_set(errado), self._test_set (atualf)
        return accuracy(self._classifier, self._test_set) 
    
    def getClassification(self):
        return self._classifier.classify(self._featurized_test_sentence)
    
    def getProbabilityAllClasses(self):
        """
        @return: One probability list for all 'classes'
        """
        # Probability dicionary class 
        dictProbs = self._classifier.prob_classify(self._featurized_test_sentence)
        probLabels = []
        for label in dictProbs.samples():
            probLabels.append((label, "{0:.4f}".format(dictProbs.prob(label))))
        probLabels.sort(key=lambda x: x[1], reverse=True)# Ordena decrescente pelo segundo termo da tupla
        return probLabels
    
    def runTrain(self):
        prePt.applyRemovalStopwordsPreTrainSet()
        trainSet = prePt.applyCleanSentencesTrainSet()
        self.trainCustom(trainSet)
        print("\n\t[LOG] - NaiveBayesCustom runTrain \n")
    
    def getProbMaxClassification(self):
        return float(self.getProbabilityAllClasses()[0][1])
    
    def getProbMinClassification(self):
        lastIndex = len(self.getProbabilityAllClasses())-1
        return float(self.getProbabilityAllClasses()[lastIndex][1])
    
    def classifyTextFromIM(self, text):
        text = pt.applyTokenizer(text)
        text = pt.applyRemovalStopwordsByList(text)
        text = pt.cleanText(text)
        text = pt.lowerCase(text)
        
        ''' REFATORAR ? ''' 
        prePt.applyRemovalStopwordsPreTrainSet()
        trainSet = prePt.applyCleanSentencesTrainSet()
        self.trainCustom(trainSet)
        
        self.test(text)
        