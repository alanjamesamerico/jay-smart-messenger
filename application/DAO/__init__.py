import pymongo

from application.DAO.campaign_dao import CampaignDAO
from application.DAO.hashtag_dao import HashtagDAO
from application.DAO.message_dao import MessageDAO


__conn__        = "mongodb://localhost"
__connection__  = pymongo.MongoClient(__conn__)

database        = __connection__.pln

messages    = MessageDAO(database)
hashtags    = HashtagDAO(database)
campaigns   = CampaignDAO(database)
