'''
Created on 6 de mai de 2017

@author: Alan James
'''
from application.naive_bayes_custom.processing_text import ProcessingText
from application.naive_bayes_custom import _LEXICON

pt = ProcessingText()

class PreProcessingText(object):
    
    def __init__(self):
        '''
        Constructor
        '''
    '''
    def applyRemovalStopwordsPreTrainSet(self):
        return pt.cleanListWords(pt.applyRemovalStopwordsByList(list(_LEXICON)))
    '''
    def applyRemovalStopwordsPreTrainSet(self):
        return pt.applyRemovalStopwordsByList(list(_LEXICON))

    def applyStemmerPreTrainSet(self):
        return pt.cleanListWords(pt.applyStemmersByList(list(_LEXICON)))
    
    def applyCleanSentencesTrainSet(self):
        return pt.cleanListWords(list(_LEXICON))
    
    def applyRemovalStopwordsPreTestSet(self, text):
        return pt.applyRemovalStopwords(text)
        
    def applyStemmerPreTestSet(self, text):
        return pt.applyStemmer(text)
    
    
        
if __name__ == '__main__':
    text = "eu estou com fome!"
    preProcess = PreProcessingText()
    #preProcess.applyRemovalStopwordsPreTrainSet()
    #preProcess.applyStemmerPreTrainSet()
    #preProcess.applyRemovalStopwordsPreTestSet(text)
    #preProcess.applyStemmerPreTestSet(text)