# -*- coding: utf-8 -*
'''
Created on 26 de ago de 2016

@author: Alan James
Estudar
=======
http://web.mit.edu/6.863/spring2011/packages/nltk-0.9.7/nltk/test/portuguese_en.doctest
'''
import json
import nltk
from unicodedata import normalize

from nltk.corpus import floresta
from nltk.corpus import mac_morpho
from nltk.corpus import stopwords

words_mm       = mac_morpho.words()
words_florest  = floresta.words()

tags_mm         = mac_morpho.tagged_words()
tags_florest    = floresta.tagged_words()

sents_florest   = floresta.tagged_sents()
sents_mm        = mac_morpho.tagged_sents() # doctest: +NORMALIZE_WHITESPACE

stop_word = stopwords.words('portuguese')
#print (stop_word)

def remove_accents(txt):
    return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')

def words_for_json():
    jwords = []
    for word in tags_mm[:20]:
        _word = remove_accents(word[0]).lower() 
        _gramatical = word[1]
        object = {'gramatical_class':_gramatical, 'word':_word}
        jwords.append(object)
    
    full_json = {'copus':'Mac Morpho', 'tags':jwords}
    _json = json.dumps(full_json, indent=2, sort_keys = True)
    
    archive = open ('C:\\Users\\alan.james\\Desktop\\macmorpho.json', 'w')
    archive.write(str(_json))
    archive.close
    print (_json)

def words_for_json_by_gramatical():
    jwords = []
    for word in tags_mm[:20]:
        _word = remove_accents(word[0]).lower() 
        _gramatical = word[1]
        object = {'gramatical_class':_gramatical, 'word':_word}
        jwords.append(object)
        
        if (_gramatical == "ADJ"):
            pass
        elif (_gramatical == "ADV"):
            pass
        elif (_gramatical == "ADV-KS"):
            pass
        elif (_gramatical == "ADV-KS-REL"):
            pass
        elif (_gramatical == "ART"):
            pass
        elif (_gramatical == "KC"):
            pass
        elif (_gramatical == "IN"):
            pass
        elif (_gramatical == "N"):
            pass
        elif (_gramatical == "NPROP"):
            pass
        elif (_gramatical == "NUM"):
            pass
        elif (_gramatical == "PCP"):
            pass
        elif (_gramatical == "PDEN"):
            pass
        elif (_gramatical == "PREP"):
            pass
        elif (_gramatical == "PROADJ"):
            pass
        elif (_gramatical == "PRO-KS"):
            pass
        elif (_gramatical == "PROPESS"):
            pass
        elif (_gramatical == "PRO-KS-REL"):
            pass
        elif (_gramatical == "PROSUB"):
            pass
        elif (_gramatical == "V"):
            pass
        elif (_gramatical == "VAUX"):
            pass
        elif (_gramatical == "CUR"):
            pass
        
    full_json = {'copus':'Mac Morpho', 'tags':jwords}
    _json = json.dumps(full_json, indent=2, sort_keys = True)
    
    archive = open ('C:\\Users\\alan.james\\Desktop\\macmorpho.json', 'w')
    archive.write(str(_json))
    archive.close
    print (_json)

def total_words_by_class_gramatical():
    jwords = []
    verbs   = []
    adjs    = []
    props   = []

    for word in tags_mm[:500]:
        _word = remove_accents(word[0]).lower() 
        _gramatical = word[1]
        object_json = {'gramatical_class':_gramatical, 'word':_word}
        jwords.append(object_json)
    
    for o in jwords:
        if (o['gramatical_class'] == "V"):
            verbs.append(o)
        elif (o['gramatical_class'] == "ADJ"):
            adjs.append(o)
        elif ("PRO" in o['gramatical_class']):
            props.append(o)
    print ("\n\nTotal de verbos: \t", len(verbs))
    print ("Total de adjetivos: \t", len(adjs))
    print ("Total de pronomes: \t", len(props))



def show_words_sents_corpus():
    print ("----------\nMac Morpho\n----------")
    print ("Tag: \t\t\t", tags_mm[0])
    print ("Palavra: \t\t", tags_mm[0][0])
    print ("Classe gramatical: \t", tags_mm[0][1])
    
    print ("\n--------\nFlorest\n--------")
    print ("Tag: \t\t\t", tags_florest[0])
    print ("Palavra: \t\t", tags_florest[0][0])
    print ("Classe gramatical: \t", tags_florest[0][1])
    
    
    print ("\n\n\n===== SENTENÇAS =====\n\nMac Morpho SENTS\n----------")
    print ("Sentença: ", sents_mm[0])
    
    print ("\nFlorest SENTS\n--------------")
    print ("Sentença: ", sents_florest[0])

def get_total_words_mac_morpho():
    return "\n---\nTotal de palavras - Mac Morpho: " + str(len(words_mm))

def get_total_words_florest():
    return "Total de palavras - Floresta: " + str(len(words_florest))

def words_for_file_txt():
    words = []
    for word in words_florest:
        _word = remove_accents(word).lower() 
        if _word not in words:
            words.append(_word)
        else:
            pass
    words.sort()
    archive = open ('C:\\Users\\alan.james\\Desktop\\wordsFlorest.txt', 'w')
    for w in words:
        archive.write(w + '\n')
    archive.close
    print ('fim')

def read_file():
    archive = open ('C:\\Users\\alan.james\\Desktop\\wordsMM-2.txt', 'r')
    content = set(archive)
    print (content)
    
    l = []
    for i in content:
        l.append(i.replace("\n", ""))
    
    print (l)
    
    l.sort()
    lista = set(l)
    print ("set: ", lista)
    archive.close
    

def tags(text):
    for tag in tags_florest[:]:
        #if text in tag:
        if 'P+v-inf' in tag:
            print (tag)


text = 'maçã'
tags(text)
#print (get_total_words_florest())
#print (get_total_words_mac_morpho())
#print (show_words_sents_corpus())
#print (total_words_by_class_gramatical())
#print (words_for_json())
#words_for_file_txt()
#read_file()


