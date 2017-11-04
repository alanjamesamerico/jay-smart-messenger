'''
Created on 2 de nov de 2017

@author: Alan James
'''
import time

from telegram.ext import MessageHandler, Filters
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.updater import Updater

from application.naive_bayes_custom.naive_bayes_custom import NaiveBayesCustom


class TelegramMessageHandler(object):
    
    def __init__(self):
        self.updater = Updater('475775136:AAFkVNGakPSCINOHKdE6jv7MKRPZXN5WoQ4') #Token
        
    def start(self, bot, update):
        update.message.reply_text('Olá {}! Seja muito bem-vindo'.format(update.message.from_user.first_name))
        time.sleep(3)
        update.message.reply_text('Muito prazer, eu sou o Jay')
        time.sleep(3)
        update.message.reply_text('e estou aqui para te ajudar a conhecer São José dos Campos. \nVamos lá!? \õ/')

    def hello(self, bot, update):
        update.message.reply_text('Oi {}! É bom ter você por aqui :D'.format(update.message.from_user.first_name))
        time.sleep(2)
        self.reply_text('Olha... eu garanto que você não vai se arrepender!')
    
    def support(self, bot, update):
        update.message.reply_text('vejo que você precisa de ajuda uma ajuda {}'.format(update.message.from_user.first_name))
        time.sleep(2)
        update.message.reply_text('me diz o que precisa..')
        
    def mess_receive_user(self, bot, update):
        
        nbCustom = NaiveBayesCustom()
        nbCustom.classifyTextFromIM(update.message.text) # self.get_last_mess()
        place = nbCustom.getClassification()
        probMax = nbCustom.getProbMaxClassification()
        #print('\nProbabilidade Máxima: ', probMax)
        #print('\nClasse: ', place)
        if (probMax < 0.5000):
            update.message.reply_text('não consigo te orientar porque não entendi o que vc quis dizer')
        elif (probMax >= 0.5000 and probMax < 0.7500):
            update.message.reply_text('olha {}, não é certeza mas.. '.format(update.message.from_user.first_name))
            time.sleep(2)
            update.message.reply_text('talvez vc vai gostar de ir no '+place)
        elif (probMax <= 0.7500 and probMax < 0.8500):
            update.message.reply_text(place+' seria um bom lugar pra vc ir {}'.format(update.message.from_user.first_name))
        else:
            update.message.reply_text(place+' é o lugar pra vc ir com toda certeza!'.format(update.message.from_user.first_name))
    '''       
    def get_last_mess(self):
        messages = self.updater.bot.getUpdates()
        print(len(messages))
        if (len(messages) == 0):
            return ''
        else:
            print("mensagens: ", messages)
            print("Ultima msg: ", messages[len(messages)-1]['message']['text'])
            return messages[len(messages)-1]['message']['text']
    '''
    
    def run_dispatcher(self):
        self.updater.dispatcher.add_handler(CommandHandler('start', self.start))
        self.updater.dispatcher.add_handler(CommandHandler('hello', self.hello))
        self.updater.dispatcher.add_handler(CommandHandler('support', self.support))
    
        receive_msg_handler = MessageHandler([Filters.text], self.mess_receive_user)
        self.updater.dispatcher.add_handler(receive_msg_handler)
    
    def start_bot(self):
        self.run_dispatcher()
        self.updater.start_polling()
        print("\n-------------------------------------------------")
        print("|\tTelegram Bot Inicialized with Success  \t|")
        print("-------------------------------------------------\n")
        self.updater.idle()
    
    def stop_bot(self):
        self.updater.stop()