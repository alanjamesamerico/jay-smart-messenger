'''
Created on 7 de set de 2016

@author: Alan James
'''

class HashtagDAOTest(object):
    
    def __init__(self, database):
        self.db = database
        self.hashtags = database.hashtags #collection