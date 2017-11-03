'''
Created on 2 de nov de 2017

@author: Alan James
'''
from telegram.ext import MessageHandler, Filters
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.updater import Updater
from asyncio.tasks import sleep



class TelegramMessageHandler(object):
    
    global _TOKEN_
    _TOKEN_ = '475775136:AAFkVNGakPSCINOHKdE6jv7MKRPZXN5WoQ4'
    
    def __init__(self):
        self.updater = Updater(_TOKEN_)
    
    def start(self, bot, update):
        update.message.reply_text('Olá {}! Seja muito bem-vindo'.format(update.message.from_user.first_name))
        sleep(5)
        update.message.reply_text('Muito prazer, eu sou o Jay')
        sleep(20)
        update.message.reply_text('e estou aqui para te ajudar a conhecer São José dos Campos. \nVamos lá!? \õ/')


    def hello(self, bot, update):
        update.message.reply_text('Oi {}! É bom ter você por aqui :D'.format(update.message.from_user.first_name))
        sleep(3)
        update.message.reply_text('Olha... eu garanto que você não vai se arrepender!')
    
    def support(self, bot, update):
        update.message.reply_text('vejo que você precisa de ajuda uma ajuda {}'.format(update.message.from_user.first_name))
        update.message.reply_text('me diz o que precisa..')
        
    def mess_receive_user(self, bot, update):
        
        update.message.reply_text(
        'Gostaria de conhecer São José dos Campos {}?'.format(update.message.from_user.first_name)+\
        '\nEntão conte comigo pra te ajudar ;D')
    
    def get_last_mess(self):
        messages = self.updater.bot.getUpdates()
        return messages[len(messages)-1]['message']['text']
    
    def run_dispatcher(self):
        self.updater.dispatcher.add_handler(CommandHandler('start', self.start))
        self.updater.dispatcher.add_handler(CommandHandler('hello', self.hello))
        self.updater.dispatcher.add_handler(CommandHandler('support', self.support))
    
        receive_msg_handler = MessageHandler([Filters.text], self.mess_receive_user)
        self.updater.dispatcher.add_handler(receive_msg_handler)
    
    def run_bot(self):
        self.run_dispatcher()
        self.updater.start_polling()
        print("-----------------------------------------")
        print("|\tService Started on Success   \t|")
        print("-----------------------------------------\n")
        self.updater.idle()
