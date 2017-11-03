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
#('Gosto de Video Game', 'BOA'),
#('Eu amo este sanduíche.', 'BOA'),
('Meu pai é o melhor', 'BOA'),
('Pessoas legais são pessoas boas!', 'BOA'),
('Este é um lugar incrível!', 'BOA'),
("Eu me sinto muito bem com essas cervejas.", "BOA"),
('Este é o meu melhor trabalho.', 'BOA'),
("Que visão fantástica", "BOA"),
("O dia esta lindo", "BOA"),
("Hoje estou BOA", "BOA"),
("Hoje eu estou muito bem", "BOA"),
("conversei com meus amigos ontem", "BOA"),
("Briguei com minha namorada", "RUIM"),
('Você está com dor de cabeça', 'RUIM'),
('Nunca mais falo com você', 'RUIM'),
('Estou irado!', 'RUIM'),
('Não como neste restaurante', 'RUIM'),
("Estou cansado dessas coisas.", "RUIM"),
("Eu não BOAso lidar com isso", "RUIM"),
("Ele é meu inimigo jurado!", "RUIM"),
("Aquela música é ruim", "RUIM"),
#("Meu computador quebrou", "RUIM"),
#("Perdi o emprego", "RUIM"),
("Não gosto de ouvir você!", "RUIM")]
'''

train = [
('Meu pai é o melhor', 'BOA'),
('Pessoas legais são pessoas boas!', 'BOA'),
('Este é um lugar incrível!', 'BOA'),
("Eu me sinto muito bem com essas cervejas.", "BOA"),
('Este é o meu melhor trabalho.', 'BOA'),
#("Briguei com minha namorada", "RUIM"),
('Você está com dor de cabeça', 'RUIM'),
('Nunca mais falo com você', 'RUIM'),
('Estou irado!', 'RUIM'),
('Não como neste restaurante', 'RUIM')]

ALL_WORDS = set(word.lower() for passage in train for word in word_tokenize(passage[0], language='portuguese'))

_LANGUAGE = 'portuguese'

_TEXT = "as vezes você age de forma estranha" #"Eu não gosto quando você faz isso!" #Eu não gosto disso cara!

CLASSIFIER = None


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
    
def word_feats(words):
    return dict([(word, True) for word in words])

def isPunct(word):
    return word in string.punctuation #len(word) == 1 and

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

def applyStemmer():
    global ALL_WORDS
    allWords = list(ALL_WORDS)
    for word in allWords:
        l = list(ALL_WORDS)
        l[l.index(word)] = RSLPStemmer().stem(word)
        ALL_WORDS = set(l)
    print("Stemmers: ", ALL_WORDS)

def testStemmer():
    print(RSLPStemmer().stem("Faz"))
    print(RSLPStemmer().stem("não"))
    print(RSLPStemmer().stem("gosto"))

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

def clearText(text):
    wordSet = set(word.lower() for word in word_tokenize(text, language=_LANGUAGE))
    #print("Tokenize: ", wordSet)
    wordSetCopy = wordSet.copy()
    stopWords = set(stopwords.words(_LANGUAGE))
    for word in wordSetCopy:
        if word in stopWords or isPunct(word[0]) or isDigits(word[0]): 
            wordSet.remove(word)
        #print(wordSet)
    newText = ''
    for word in wordSet:
        newText = newText + word + ' '
    print("new text: ", newText)
    return newText

def clearSWAndStemmers(text):
    wordSet = set(word.lower() for word in word_tokenize(text, language=_LANGUAGE))
    wordSetCopy = wordSet.copy()
    
    # Remove STOPWORDS
    stopWords = set(stopwords.words(_LANGUAGE))
    for word in wordSetCopy:
        if word in stopWords or isPunct(word[0]) or isDigits(word[0]): 
            wordSet.remove(word)
        #print(wordSet)
    #newText = ''
    
    textFinal = []
            
    # Aplica STEMMER
    wordSetList = list(wordSet)
    l = list(wordSet)
    for word in wordSetList:
        #l = list(wordSet)
        l[l.index(word)] = RSLPStemmer().stem(word)
    textFinal = set(l)
    print("Stemmers: ", textFinal)
    newText = ''
    for word in textFinal:
        newText = newText + word + ' '
    print("new text: ", newText)
    return newText
    #return textFinal
    
def nltkNativeDemo():
    
    #all_words = set(word.lower() for passage in train for word in word_tokenize(passage[0], language='portuguese'))
    all_words = set(isDigits(isPunct(word.lower())) for passage in train for word in word_tokenize(passage[0], language='portuguese'))
    print("\nALL WORDS: \n%s" %all_words)
    
    test_set = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in train]
    #print("\n\nTEST SET: \n%s" %test_set)
    
    classifier = NaiveBayesClassifier.train(test_set)
    
    # Tratar _TEXT com stopwrds e stemmers
    
    featurized_test_sentence = {word.lower(): (word in word_tokenize(_TEXT.lower())) for word in all_words}
    #print("\n\nTEST SENT FEATUURE: \n%s" %featurized_test_sentence)
    #print("\nClassification: %s" %classifier.classify(featurized_test_sentence), "\nAccuracy: %.4f" %nltk.classify.accuracy(classifier, test_set))
    print("Accuracy: %.2f" %nltk.classify.accuracy(classifier, test_set))
    
    # Probabilidade por 'labels'
    dictProbs = classifier.prob_classify(featurized_test_sentence) 
    #print("\nProbability\n---\nBOA: %.4f\nRUIM: %.4f" %(dictProbs.prob('BOA'), dictProbs.prob('RUIM')))
    
    probLabels = []
    for label in dictProbs.samples():
        probLabels.append((label, dictProbs.prob(label)))
    probLabels.sort(reverse=True)
    for content in probLabels:
        print("%s\t\t - %.4f" %(content[0], (round(content[1], 2))))

# Função que auxilia a fazer o treino em memória    
def extractFeature(document):
    return {word.lower(): (word in set(document)) for word in ALL_WORDS}
    #return {'contains(%s)'% word.lower(): (word in set(document)) for word in ALL_WORDS}
    
def trainInMemory():
    global CLASSIFIER
    
    test_set = [({word: (word in word_tokenize(x[0])) for word in ALL_WORDS}, x[1]) for x in train]
    
    training_set = apply_features(extractFeature, test_set)
    
    print("\n> Training Set: ", training_set)
    
    CLASSIFIER = NaiveBayesClassifier.train(training_set)
    
    '''
    print("Other Classifier: ", CLASSIFIER.classify(word_feats([_TEXT])), "\n\n\t> List: ", list(word_feats([_TEXT])))
    for i in list(word_feats([_TEXT])):
        print("\t> ", i)
    print("\nClassification: %s" %CLASSIFIER.classify(word_feats([_TEXT])),"\nAccuracy: %.4f" %nltk.classify.accuracy(CLASSIFIER, test_set))
    '''
    
    '''
    @note: Aplicação de PLN no texto para teste
    '''
    text = clearSWAndStemmers(_TEXT)
    print(">> Texto tratado: ", text)
    
    featurized_test_sentence = {word.lower(): (word in word_tokenize(text, language=_LANGUAGE)) for word in ALL_WORDS}
    print("\nfeaturized_test_sentence: ", featurized_test_sentence)
    
    print("\nClassification MAX: %s" %CLASSIFIER.classify(featurized_test_sentence),
          "\nAccuracy: %.4f" %nltk.classify.accuracy(CLASSIFIER, training_set))
    
    #for i in training_set:
        #print("---\nDict: " , i[0], "\nLabel: ", i[1], "\nClassification: ", CLASSIFIER.classify(i[0]))
    
    # Probabilidade por 'labels'
    dictProbs = CLASSIFIER.prob_classify(featurized_test_sentence)
    #dictProbs = CLASSIFIER.prob_classify(word_feats([_TEXT]))
    probLabels = []
    for label in dictProbs.samples():
        probLabels.append((label, "{0:.5f}".format(dictProbs.prob(label))))
    probLabels.sort(key=itemgetter(0)) #(key=lambda tup: tup[0])
    print("Probabiliteis => [%s: %s] - [%s: %s]" %(probLabels[0][0], probLabels[0][1], probLabels[1][0], probLabels[1][1]))

if __name__ == '__main__':
    #print("All Words: ", ALL_WORDS)
    
    print("Text: %s" %_TEXT,"\n\nNATIVO\n======")
    trainInMemory()
    
    '''
    print("\nC/ STEMMER\n==========")
    applyStemmer()
    trainInMemory()
    
    print("\nS/ STOP WORDS\n=================")
    removeStopWords()
    trainInMemory()
    #nltkNativeDemo()
    '''
    #print(clearText("Eu não gosto muito de batata frita =/ mas hamburguer é 10!"))
    print('\n\n## End Test ##')