'''
Created on 7 de set de 2016

@author: Alan James
'''

from pymongo import MongoClient
import json

class CampaingDAOTest(object):
    
    def __init__(self):
        __conn__    = "localhost"
        __port__    = 27017        
        __connection__  = MongoClient(__conn__, __port__)

        self.db         = __connection__.pln
        self.campaigns  = self.db.campaigns #collection
    
    def findAllCampaings(self):
        return self.campaigns.find()
    
    

campaigns = CampaingDAOTest().findAllCampaings()

for doc in campaigns:
    print (doc)