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

'''
train = [
#('Gosto de Video Game', 'POS'),
#('Eu amo este sanduíche.', 'POS'),
('Meu pai é o melhor', 'POS'),
('Pessoas legais são pessoas boas!', 'POS'),
('Este é um lugar incrível!', 'POS'),
("Eu me sinto muito bem com essas cervejas.", "POS"),
('Este é o meu melhor trabalho.', 'POS'),
("Que visão fantástica", "POS"),
("O dia esta lindo", "POS"),
("Hoje estou feliz", "POS"),
("Hoje eu estou muito bem", "POS"),
("conversei com meus amigos ontem", "POS"),
("Briguei com minha namorada", "NEG"),
('Você está com dor de cabeça', 'NEG'),
('Nunca mais falo com você', 'NEG'),
('Estou irado!', 'NEG'),
('Não como neste restaurante', 'NEG'),
("Estou cansado dessas coisas.", "NEG"),
("Eu não posso lidar com isso", "NEG"),
("Ele é meu inimigo jurado!", "NEG"),
("Aquela música é ruim", "NEG"),
#("Meu computador quebrou", "NEG"),
#("Perdi o emprego", "NEG"),
("Não gosto de ouvir você!", "NEG")]
'''

train = [
('Meu pai é o melhor', 'POS'),
('Pessoas legais são pessoas boas!', 'POS'),
('Este é um lugar incrível!', 'POS'),
("Eu me sinto muito bem com essas cervejas.", "POS"),
('Este é o meu melhor trabalho.', 'POS'),

#("Briguei com minha namorada", "NEG"),
('Você está com dor de cabeça', 'NEG'),
('Nunca mais falo com você', 'NEG'),
('Estou irado!', 'NEG'),
('Não como neste restaurante', 'NEG')]

ALL_WORDS = set(word.lower() for passage in train for word in word_tokenize(passage[0], language='portuguese'))
_LANGUAGE = 'portuguese'

_TEXT = "não gosto dessa brincadeira"

CLASSIFIER = None

def word_feats(words):
    return dict([(word, True) for word in words])

def isPunct(word):
    return len(word) == 1 and word in string.punctuation

def isDigits(word):
    return word in string.digits

def removeStopWords():
    print("Antes: ", ALL_WORDS)
    stopWords = set(stopwords.words(_LANGUAGE))
    allWords = list(ALL_WORDS)
    for word in allWords:
        if word in stopWords or isPunct(word):
            #print("Excluido > ", word)
            ALL_WORDS.remove(word)
    print("Depois: ", ALL_WORDS)     

def treatTokens():
    #print(RSLPStemmer().stem('Viajando'))
    print("Depois: ", ALL_WORDS)
    global ALL_WORDS
    stopWords = set(stopwords.words(_LANGUAGE))
    allWords = list(ALL_WORDS)
    for word in allWords:
        if word in stopWords or isPunct(word) or isDigits(word):
            #print("Excluido > ", word)
            ALL_WORDS.remove(word)
        else:
            l = list(ALL_WORDS)
            l[l.index(word)] = RSLPStemmer().stem(word)
            ALL_WORDS = set(l)
    print("Stemmers: ", ALL_WORDS)

def applyStemmer():
    global ALL_WORDS
    allWords = list(ALL_WORDS)
    for word in allWords:
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
    #print("Training Set: ", training_set)
    CLASSIFIER = NaiveBayesClassifier.train(training_set)
    
    '''
    print("Other Classifier: ", CLASSIFIER.classify(word_feats([_TEXT])), "\n\n\t> List: ", list(word_feats([_TEXT])))
    for i in list(word_feats([_TEXT])):
        print("\t> ", i)
    print("\nClassification: %s" %CLASSIFIER.classify(word_feats([_TEXT])),"\nAccuracy: %.4f" %nltk.classify.accuracy(CLASSIFIER, test_set))
    '''
    
    featurized_test_sentence = {word.lower(): (word in word_tokenize(_TEXT.lower(), language=_LANGUAGE)) for word in ALL_WORDS}
    
    #print("\nfeaturized_test_sentence: ", featurized_test_sentence)
    print("Classification MAX: %s" %CLASSIFIER.classify(featurized_test_sentence),"\nAccuracy: %.4f" %nltk.classify.accuracy(CLASSIFIER, training_set))
    
    #for i in training_set:
        #print("---\nDict: " , i[0], "\nLabel: ", i[1], "\nClassification: ", CLASSIFIER.classify(i[0]))
    
    # Probabilidade por 'labels'
    dictProbs = CLASSIFIER.prob_classify(featurized_test_sentence)
    #dictProbs = CLASSIFIER.prob_classify(word_feats([_TEXT]))
    probLabels = []
    for label in dictProbs.samples():
        probLabels.append((label, "{0:.5f}".format(dictProbs.prob(label))))
    probLabels.sort(key=itemgetter(0)) #(key=lambda tup: tup[0])
    print("Probabiliteis => %s: %s - %s: %s" %(probLabels[0][0], probLabels[0][1], probLabels[1][0], probLabels[1][1]))

if __name__ == '__main__':
    #print("All Words: ", ALL_WORDS)
    print("Text: %s" %_TEXT,"\n\nNORMAL\n======")
    trainInMemory()
    
    print("\nC/ STEMMER\n==========")
    applyStemmer()
    trainInMemory()
    
    print("\nS/ STOPWORDS e C/ STEMMERS\n=================")
    removeStopWords()
    trainInMemory()
    #nltkNativeDemo()
    
    print('\n\n## End Test ##')