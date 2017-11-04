'''
Created on 2 de nov de 2017

@author: Alan James
'''
import os

from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler

from application.im.telegram.telegram_message_handler import TelegramMessageHandler


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


URL_PROD = 'https://jay-smart-messenger.herokuapp.com'
URL_TEST = ''
PORT = int(os.environ.get("PORT", 8000))

'''
    CONFIG ROUTES
    --------------
'''
application = Application([
        (r"/", MainHandler),
        (r"/bot/start", TelegramBotStart),
        (r"/bot/stop", TelegramBotStop),
])


def ru_server_prod():
    application.listen(PORT, URL_PROD)
    IOLoop.instance().start()

def run_server():
    application.listen(port=PORT, address=URL_TEST) #Test Default
    print("\n\t[LOG] - Server Initialized")
    IOLoop.instance().start()