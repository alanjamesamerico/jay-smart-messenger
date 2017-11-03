'''
Created on 1 de nov de 2017

@author: Alan James
'''
import requests
from asyncio.tasks import sleep


URL = "https://api.telegram.org/bot475775136:AAFkVNGakPSCINOHKdE6jv7MKRPZXN5WoQ4/"

def get_updates_json(request):  
    response = requests.get(request + 'getUpdates')
    return response.json()

def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(URL + 'sendMessage', data=params)
    return response

#chat_id = get_chat_id(last_update(get_updates_json(URL)))
#send_mess(chat_id, 'Your message goes here')
'''
def run_bot():
    print("\n\t --- Bot Inicializado ---")
    update_id = last_update(get_updates_json(URL))['update_id']
    while True:
        if update_id == last_update(get_updates_json(URL))['update_id']:
            # Handler Message - message text - message foto 
            send_mess(get_chat_id(last_update(get_updates_json(URL))), 'Salve !')
            update_id += 1
    sleep(1)       

if __name__ == '__main__':
    run_bot()
'''