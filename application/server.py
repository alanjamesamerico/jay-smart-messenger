'''
Created on 1 de nov de 2017

@author: Alan James
'''
import tornado.ioloop
import tornado.web
from application.im_bot.telegram_handler import run_bot

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
    def startTelegramBot(self):
        pass
        #TelegramHandler.run_bot(self)

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/star/bot", MainHandler.startTelegramBot()),
])

if __name__ == "__main__":
    application.listen(8000, address='127.0.0.1')
    print("Server listening on port 8000...")
    tornado.ioloop.IOLoop.instance().start()
