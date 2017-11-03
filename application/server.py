'''
Created on 1 de nov de 2017

@author: Alan James
'''
import tornado.ioloop
from tornado.web import RequestHandler, Application

from application.im.telegram.telegram_message_handler import TelegramMessageHandler


class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello, world")
        
class TelegramBot(RequestHandler):    
    def get(self):
        self.write("Start Bot Telegram")
        telegram_bot = TelegramMessageHandler()
        print("\n\tTelegramBot Log...\n")
        telegram_bot.run_bot()
        #run_bot()
        
URL_PROD = 'https://jay-smart-messenger.herokuapp.com'
URL_TEST = ''

application = Application([
    (r"/", MainHandler),
    (r"/start/bot", TelegramBot)
])

application.listen(URL_PROD)

'''
def server_local():
    applicationTest = Application([
        (r"/", MainHandler),
        (r"/start/bot", TelegramBot)
    ])
    applicationTest.listen(8000, URL_TEST)
    print("Server listening on port 8000 in Localhost...")
    tornado.ioloop.IOLoop.instance().start()

server_local()
'''