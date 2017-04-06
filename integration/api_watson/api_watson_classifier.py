'''
Created on 28 de nov de 2016

@author: alan.james
'''
'''
Created on 25 de ago de 2016

@author: Alan James
'''

import json
from watson_developer_cloud import NaturalLanguageClassifierV1

class APIWatson(object):
    
    def __init__ (self):
        __user__ = "a2604041-baf2-4b33-9a4b-1a5c105d27c6"
        __pass__ = "KfdJeYILq47S" 
        self.classifier_id = "ff189ax155-nlc-5003"
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
    
    def getClassify (self, text):
        classes = self.auth.classify(self.classifier_id, text)
        return (json.dumps(classes,indent=2))
