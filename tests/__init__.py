from pymongo import MongoClient

from tests.DAO.campaign_dao_test import CampaingDAOTest
from tests.DAO.hashtag_dao_test import HashtagDAOTest
from tests.DAO.message_dao_test import MessageDAOTest



__conn__    = "localhost"
__port__    = 27017        
__connection__  = MongoClient(__conn__, __port__)

database        = __connection__.pln

messages    = MessageDAOTest(database)
hashtags    = HashtagDAOTest(database)
campaigns   = CampaingDAOTest(database)