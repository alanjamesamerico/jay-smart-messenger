'''
Created on 9 de jan de 2017

@author: alan.james
'''
# ' ATENCAO - Antes de executar:
# ' pip install requests
# ' pip install pprint
import json, requests

def classify(text):
    url = 'Http://services.socialchatter.com.br/classify'
    payload = {
        'idCampaign':'58739f9fa39f7c6efa17f422',
        'language':'pt',
        'text':text
    }
    headers = {
        'sc-auth-token': 'cY5RUDrYuea9XaIT7z7atrjAa+dUtYEoRykHDR2Qfxw+uBmAqeC9JbUJvQpSo5l8pjdfNKPxhSvw+9EBzhHLf1RPIpzdiFNsxOCRb/Kan38=',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    resp = requests.post(url, data=payload, headers=headers)
    return json.loads(resp.text)
