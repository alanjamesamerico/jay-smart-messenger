'''
Created on 26 de ago de 2016

@author: Alan James
'''
from api_watson.api_watson_nlc import APIWatson
import json

class TextBO(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def process_text (self, text):
        words = []
        for word in text:
            word.append(word)
        
        analyses = api.getClassify(api.c_id, text)
        return analyses
    

api = APIWatson ()