'''
Created on 2 de nov de 2017

@author: Alan James
'''
import os

from tornado.ioloop import IOLoop

from application.routes import MainHandler, TelegramBotStart, TelegramBotStop
from tornado.web import Application


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