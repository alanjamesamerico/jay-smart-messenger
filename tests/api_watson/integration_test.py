'''
Created on 25 de ago de 2016

@author: Alan James
'''

from application.api_watson.api_watson_nlc import APIWatson


class testsIntegration (object):
    
    def __init__(self):
        self.__text__ = ""
        self.wapi = APIWatson
        self.c_id = "340008x87-nlc-2365"
        
    def test_clazzify(self):
        print (self.wapi.clazzify(self.c_id, self.__text__))
        


