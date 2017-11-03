'''
Created on 2 de nov de 2017

@author: Alan James
'''
import os

from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from application.im.telegram.telegram_message_handler import TelegramMessageHandler

telegram_bot = TelegramMessageHandler()

class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello, world")
        
class TelegramBot(RequestHandler):    
    def get(self):
        self.write("Start Bot Telegram")
        print("\n\t[LOG] - TelegramBot Started...\n")
        telegram_bot.start_bot()

class TelegramBotStart(RequestHandler):
    def get(self):
        self.write("Serviço do Telegram Bot Parado!")
        print("\n\t[LOG] - TelegramBot Stopped...\n")
        telegram_bot.stop_bot()


URL_PROD = 'https://jay-smart-messenger.herokuapp.com'
URL_TEST = ''
PORT = int(os.environ.get("PORT", 8000))


def server_prod():
    application = Application([
        (r"/", MainHandler),
        (r"/start/bot", TelegramBot)
    ])
    application.listen(PORT, URL_PROD)
    IOLoop.instance().start()

def server_local():
    applicationTest = Application([
        (r"/", MainHandler),
        (r"/start/bot", TelegramBot)
    ])
    applicationTest.listen(port=PORT, address=URL_TEST)
    print("Server listening on port 8000 in Localhost...")
    IOLoop.instance().start()
