'''
Created on 26 de ago de 2016

@author: Alan James
'''
import json
from application.api_watson.api_watson_nlc import APIWatson

class TextBO(object):

    def __init__(self):
        pass
    
    def process_text (self, text):
        
        # OK - enviar texto para analise do Watson
        # OK - pegar o retorno do watson e classificar em ordem decrescente os scores de cada class (fazer um dicionario)
        
        # pegar as hashtags relacionadas com campanha da msg enviada
        # verificar se a classe de maior score esta nas hashtags
        # retornar o conteudo para a hashtag encontrada
        
        analyses = api.getClassify(api.c_id, text)
        
        TextBO.process_return_watson(self, analyses)
        
        words = []
        for word in text:
            word.append(word)
        
        return analyses
    
    def process_return_watson(self, processed_text):
        
        for content in processed_text:
            print (content)
        
    
api = APIWatson ()