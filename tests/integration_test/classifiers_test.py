'''
Created on 28 de nov de 2016

@author: alan.james

##############################################
#                   TESTS                    #
##############################################
'''
from integration.api_watson.api_watson_classifier import APIWatson
from integration.sc_texBlob.text_blob_classifier import train_data,\
    get_all_prob_labels
from integration.sc_lingpipe.sc_lingpipe_classifier import classify
import pprint


_FILEPATH_JOB = 'C:\\Users\\alan.james\\Desktop\\bonito-turista-atrativos-train-2.csv' #train-test-TextBlob.csv
_FILEPATH_HOME = 'C:\\bonito-turista-atrativos-train-2.csv'
#C:\\Users\\Alan\ James\\Desktop\\bonito-turista-atrativos-train-2.csv

_TEXT = 'andar'

wapi = APIWatson()
classifier = train_data(_FILEPATH_HOME)
prob_dist = classifier.prob_classify(_TEXT)
    
def lingPipeTest():
    result = classify(_TEXT)
    print ("\nLingpipe: ")
    pprint.pprint(result)

def textBlobTest():
    print("\n\nTEXT BLOB Classifier\n====================\n\nTop Class: " + prob_dist.max())
    labels = get_all_prob_labels(classifier, _TEXT)
    print("\nProbabilidades:\n---\n")
    for i in range(0, len(labels)):
        print(labels[i])

def watsonApiTest():
    print("WATSON Classifier\n================\n" + wapi.getClassify(_TEXT))

'''
def textBlob_x_lingPipeTest():
    listText = [
    'onde eu posso nadar?',
    'quero mergulhar',
    'quero fazer trilha e pedalar',
    'gosto de cobra',
    'onde eu posso fazer boiacross?',
    'aqui tem passeio a cavalo?',
    'trilha',
    'gosto de fazer trilha',
    'quero correr',
    'passeio de bicicleta',
    'aqui tem algum rio?',
    'onde eu posso comer?',
    'andar de bike',
    'quero cavalgar no rio',
    'aqui na cidade tem alguma gruta?',
    'quero fazer rapel',
    'quero dar um mergulho',
    'gosto de mergulhar',
    'quero ver uma nascente',
    'aqui tem cachoeiras',
    'onde eu posso fazer flutuação',
    'quero beber',
    'onde tem aquário?',
    'quero visitar um aquário',
    'gosto de arborismo',
    'gosto de andar na mata'
    ]
    
    for text in listText:
        prob_dist = classifier.prob_classify(text)
        print("\n\n-----\nTexto: ", text, "\n-----\n")
        print("TEXTBLOB\n---\nTop Class: " + prob_dist.max(), "\n")
        labels = get_all_prob_labels(classifier, text)
        for i in range(0, len(labels)):
            if (labels[i][1] != 0.0): print(labels[i])
            else: pass
        
        result = classify(text)
        print ("\nLINGPIPE\n---\n ")
        pprint.pprint(result)
'''
    
#watsonApiTest()
textBlobTest()
#textBlob_x_lingPipeTest()
#lingPipeTest()
