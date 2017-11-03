'''
from http.server import HTTPServer

from tornado.ioloop import IOLoop
from tornado.routing import RuleRouter, Rule, HostMatches, PathMatches
from tornado.web import Application
from tornado.web import RequestHandler

from application.im.telegram.telegram_message_handler import TelegramMessageHandler


class MainHandler(RequestHandler):
    def get(self):
        self.write(";D Hello, world")
        
class TelegramBot(RequestHandler):    
    def get(self):
        self.write("Start Bot Telegram")
        telegram_bot = TelegramMessageHandler()
        #telegram_bot.run_bot()
        #run_bot()


"""
############################
        SEVER CONFIG
############################
"""
PORT    = 8000
ADDRESS = '' #127.0.0.1
MSG_SERVER = \
"-----------------------------------------\n\
|\tServer on in - localhost:"+str(PORT)+"\t|"\
"\n-----------------------------------------\n"

application = Application([
   (r"/", MainHandler),
   (r"/start/bot", TelegramBot)
])


def run_server():
    application.listen(PORT)
    print(MSG_SERVER)
    IOLoop.instance().start()

if __name__ == '__main__':
    run_server()
'''