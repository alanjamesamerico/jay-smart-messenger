'''
Created on Apr 1, 2017

@author: Alan James
'''

from nltk import NaiveBayesClassifier
import nltk
from nltk.classify.util import apply_features
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer
import string
from _operator import itemgetter


train = [
('Eu amo este sanduíche.', 'POS'),
('Meu pai é o melhor', 'POS'),
('Pessoas legais são pessoas boas!', 'POS'),
('Este é um lugar incrível!', 'POS'),
("Eu me sinto muito bem com essas cervejas.", "POS"),
('Este é o meu melhor trabalho.', 'POS'),
("Que visão fantástica", "POS"),
('Não como este restaurante', 'NEG'),
("Estou cansado dessas coisas.", "NEG"),
("Eu não posso lidar com isso", "NEG"),
("Ele é meu inimigo jurado!", "NEG"),
("Aquela música é ruim", "NEG"),
("Não gosto de ouvir você!", "NEG")]

ALL_WORDS = set(word.lower() for passage in train for word in word_tokenize(passage[0], language='portuguese'))
_LANGUAGE = 'portuguese'

_TEXT = "que lugar lindo"

CLASSIFIER = None

def isPunct(word):
    return len(word) == 1 and word in string.punctuation

def removeStopWords():
    stopWords = set(stopwords.words(_LANGUAGE))
    allWords = list(ALL_WORDS)
    for word in allWords:
        if word in stopWords or isPunct(word):
            #print("Excluido > ", word)
            ALL_WORDS.remove(word)

def treatTokens():
    #print(RSLPStemmer().stem('Viajando'))
    removeStopWords()
    print("Depois: ", ALL_WORDS)
    global ALL_WORDS
    stopWords = set(stopwords.words(_LANGUAGE))
    allWords = list(ALL_WORDS)
    for word in allWords:
        if word in stopWords or isPunct(word):
            #print("Excluido > ", word)
            ALL_WORDS.remove(word)
        else:
            l = list(ALL_WORDS)
            l[l.index(word)] = RSLPStemmer().stem(word)
            ALL_WORDS = set(l)
    print("Stemmers: ", ALL_WORDS)  

'''
VER ERRO
'''
def getProbsLabels(dictProbs):
    probLabels = []
    for label in dictProbs.samples():
        probLabels.append((label, dictProbs.prob(label)))
    return probLabels.sort(reverse=True)

def nltkCustomerDemo():
    pass


def nltkNativeDemo():
    all_words = set(word.lower() for passage in train for word in word_tokenize(passage[0], language='portuguese'))
    #print("ALL WORDS: \n%s" %all_words)
    
    test_set = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in train]
    #print("\n\nTEST SET: \n%s" %test_set)
   
    classifier = NaiveBayesClassifier.train(test_set)
    
    featurized_test_sentence = {word.lower(): (word in word_tokenize(_TEXT.lower())) for word in all_words}
    #print("\n\nTEST SENT FEATUURE: \n%s" %featurized_test_sentence)
    #print("\nClassification: %s" %classifier.classify(featurized_test_sentence), "\nAccuracy: %.4f" %nltk.classify.accuracy(classifier, test_set))
    print("Accuracy: %.2f" %nltk.classify.accuracy(classifier, test_set))
    
    # Probabilidade por 'labels'
    dictProbs = classifier.prob_classify(featurized_test_sentence) 
    #print("\nProbability\n---\nPOS: %.4f\nNEG: %.4f" %(dictProbs.prob('POS'), dictProbs.prob('NEG')))
    
    probLabels = []
    for label in dictProbs.samples():
        probLabels.append((label, dictProbs.prob(label)))
    probLabels.sort(reverse=True)
    for content in probLabels:
        print("%s\t\t - %.4f" %(content[0], (round(content[1], 2))))

    
def extractFeature(document):
    return {word.lower(): (word in set(document)) for word in ALL_WORDS}
    #return {'contains(%s)'% word.lower(): (word in set(document)) for word in ALL_WORDS}
    
def trainInMemory():
    
    global CLASSIFIER
    
    test_set = [({word: (word in word_tokenize(x[0])) for word in ALL_WORDS}, x[1]) for x in train]
    training_set = apply_features(extractFeature, test_set)
    print("Training Set: ", training_set)
    CLASSIFIER = NaiveBayesClassifier.train(training_set)
    
    featurized_test_sentence = {word.lower(): (word in word_tokenize(_TEXT.lower(), language=_LANGUAGE)) for word in ALL_WORDS}
    
    #print("featurized_test_sentence: ", featurized_test_sentence)
    print("\nClassification: %s" %CLASSIFIER.classify(featurized_test_sentence),"\nAccuracy: %.4f" %nltk.classify.accuracy(CLASSIFIER, test_set))
    
    # Probabilidade por 'labels'
    dictProbs = CLASSIFIER.prob_classify(featurized_test_sentence)
    probLabels = []
    for label in dictProbs.samples():
        probLabels.append((label, "{0:.4f}".format(dictProbs.prob(label))))
    probLabels.sort(key=itemgetter(0)) #(key=lambda tup: tup[0])
    print(probLabels)

if __name__ == '__main__':
    #test()
    #print("All Words: ", ALL_WORDS)
    #removeStopWords()
    #treatTokens()
    #print("Depois: ", ALL_WORDS)
    trainInMemory()
    #nltkNativeDemo()
    print('\n\n## End Test ##')