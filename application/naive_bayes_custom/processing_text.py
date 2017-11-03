'''
Created on 5 de mai de 2017

@author: Alan James
'''
from nltk.tokenize import word_tokenize
import string
from nltk.stem.rslp import RSLPStemmer
from nltk.corpus import stopwords
from application.naive_bayes_custom import _LANGUAGE

class ProcessingText():
    
    def isPunct(self,word):
        return word in string.punctuation #len(word) == 1 and
    
    def isDigits(self, word):
        return word in string.digits
    
    def applyTokenizer(self, text):
        return word_tokenize(text, _LANGUAGE)
    
    def applyStemmer(self, text):
        tokens = self.applyTokenizer(text)
        #tokensCopy = tokens
        for word in tokens:
            tokens[tokens.index(word)] = RSLPStemmer().stem(word)
        return tokens
    
    def applyStemmersByList(self, listWords):
        listWordsCopy = listWords
        for word in listWordsCopy:
            listWords[listWords.index(word)] = RSLPStemmer().stem(word)
        return listWords
    
    def applyRemovalStopwords(self, text):
        tokens = self.applyTokenizer(text)
        tokensCopy = tokens
        lStopwords = stopwords.words(_LANGUAGE)
        for word in tokensCopy:
            if word in lStopwords:
                tokens.remove(word)
        return tokens
    
    def applyRemovalStopwordsByList(self, listWords):
        lStopwords = stopwords.words(_LANGUAGE)
        listWordsCopy = listWords
        stopWordsList = []
        for word in listWordsCopy:
            if word in lStopwords:
                listWords.remove(word)
                stopWordsList.append(word)
        #print(">> Stopwords removidas: ", stopWordsList)
        return listWords
    
    def applyPOSTag(self):
        pass
    
    def cleanText_(self, text):
        tokens = self.applyTokenizer(text)
        tokensCopy = tokens
        for word in tokensCopy:
            if word in string.digits:
                tokens.remove(word)
            elif word in string.punctuation:
                tokens.remove(word)
        return tokens
    
    def cleanText(self, listWords):
        newListWords = listWords
        for word in newListWords:
            if word in string.digits:
                newListWords.remove(word)
            elif word in string.punctuation:
                newListWords.remove(word)
        return newListWords
    
    def cleanListWords(self, listWords):
        listWordsCopy = listWords
        for word in listWordsCopy:
            if word in string.digits:
                listWords.remove(word)
            elif word in string.punctuation:
                listWords.remove(word)
        return listWords
    
    def lowerCase(self, listWord):
        for i in range(len(listWord)):
            listWord[i] = listWord[i].lower()
        return listWord
            
if __name__ == '__main__':
    #eu. fui dar-lhe, um dia! ~ certo [1 - e] desejou anotar anotação, comer comida
    
    #text = "B. C,-S ,dar-lhe ! ~A [[1  e] anotação, 1 @ C"
    text = ["SAbe", "um","DIA","você", "vaI"]
    print("Text: ", text, "\n")
    
    pt1 = ProcessingText()
    pt2 = ProcessingText()
    pt3 = ProcessingText()
    pt4 = ProcessingText()
    #print("Stemmer - ", pt1.applyStemmer("Eu gosto muito de comer batata frita"))
    #print("Tokens - ", pt2.applyTokenizer("Eu gosto muito de comer batata frita"))
    #print("Removal Stopwords - ", pt3.applyRemovalStopwords(text))
    #print("Clean - ", pt3.cleanText(text))
    print(pt4.lowerCase(text))