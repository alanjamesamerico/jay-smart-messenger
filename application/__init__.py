from tornado.web import RequestHandler
from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.routing import RuleRouter, Rule, HostMatches, PathMatches
from http.server import HTTPServer
#from application.im_bot.telegram_handler import run_bot

class MainHandler(RequestHandler):
    def get(self):
        self.write(";D Hello, world")
        
class TelegramBot(RequestHandler):    
    def get(self):
        self.write("Start Bot Telegram")
        #run_bot()
        #TelegramHandler.run_bot(self)


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

#run_server()