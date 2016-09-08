'''
Created on 25 de ago de 2016

@author: Alan James
'''

import json
from watson_developer_cloud import NaturalLanguageClassifierV1

class APIWatson(object):
    
    def __init__ (self):
        __user__ = "e5cdffc6-5f9a-47ff-bb7b-005b08c071a4"
        __pass__ = "FfbYlWjZVLwT"
        self.auth = NaturalLanguageClassifierV1(username = __user__, password = __pass__)
            
    def getAuthentication (self):
        return self.auth
    
    def listClassifiers (self):
        classifiers = self.auth.list()
        return (json.dumps(classifiers, indent=2))
    
    def getInfomationClassifier (self, classifier_id):
        info = self.auth.status(classifier_id)
        return (json.dumps(info,indent=2))
    
    def deleteClassifier (self, classifier_id):
        classes = self.auth.remove(classifier_id)
        return (json.dumps(classes,indent=2))
    
    def getClassify (self, classifier_id, text):
        classes = self.auth.classify(classifier_id, text)
        return (json.dumps(classes,indent=2))
    

        
        
        
        
        