'''
Created on 26 de ago de 2016

@author: Alan James
'''
import json

from bottle import request

from app_project import app
from app_project.bo.text_bo import TextBO


__prefix__ = "/app"

@app.get('/')
def index():
    return json.dumps({'text':'Ok'}, indent=2)

@app.post(__prefix__ + '/process/text')
def get_classify():
    response = text.process_text( request.json['text'])
    return json.dumps(response, indent=2)


text = TextBO()