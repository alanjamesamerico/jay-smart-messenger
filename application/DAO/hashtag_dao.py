'''
Created on 7 de set de 2016

@author: Alan James
'''

class HashtagDAO(object):

    def __init__(self, database):
        self.db = database
        self.hashtags = database.hashtags #collection
        