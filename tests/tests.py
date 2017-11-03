'''
Created on 8 de mai de 2017

@author: Alan James
'''

from nltk.corpus import floresta
from nltk.corpus import mac_morpho
from nltk.stem import WordNetLemmatizer


if __name__ == '__main__':
    #lemmatizer = WordNetLemmatizer()
    #print(lemmatizer.lemmatize('cooking'))
    

    wordsMM       = mac_morpho.words()
    wordsFlorest  = floresta.words()
    
    tagsMM         = mac_morpho.tagged_words()
    tags_florest   = floresta.tagged_words()
    
    for i in tagsMM:
        print(i)



'''
Exemplo de uma função apra lematizar
http://forum.language-learners.org/viewtopic.php?t=4867 -> 08/05/2017

#encoding: utf8
lemmaDict = {}
with open('lemmatization-es.txt', 'rb') as f:
   data = f.read().decode('utf8').replace(u'\r', u'').split(u'\n')
   data = [a.split(u'\t') for a in data]
   
for a in data:
   if len(a) >1:
      lemmaDict[a[1]] = a[0]
   
def lemmatize(word):
   return lemmaDict.get(word, word + u'*')
'''
