'''
Created on 2 de nov de 2017

@author: Alan James
'''

from application.im.telegram.telegram_message_handler import TelegramMessageHandler
from tornado.web import RequestHandler


telegram_bot = TelegramMessageHandler()

class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello, world")
        
class TelegramBotStart(RequestHandler):    
    def get(self):
        self.write("Start Bot Telegram")
        print("\n\t[LOG] - TelegramBot Started\n")
        telegram_bot.start_bot()

class TelegramBotStop(RequestHandler):
    def get(self):
        self.write("Serviço do Telegram Bot Parado!")
        print("\n\t[LOG] - TelegramBot Stopped\n")
        telegram_bot.stop_bot()