'''
Created on 7 de set de 2016

@author: Alan James
'''

class CampaignDAO(object):

    def __init__(self, database):
        self.db = database
        self.campaigns = database.campaigns #collection
    
    def findAllCampaings(self):
        return self.campaigns.find()
        