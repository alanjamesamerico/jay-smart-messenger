'''
Created on 26 de ago de 2016

@author: Alan James
'''

if __name__ == '__main__':
    pass

'''
Estudar
=======
http://web.mit.edu/6.863/spring2011/packages/nltk-0.9.7/nltk/test/portuguese_en.doctest
'''

import nltk
corpus = nltk.corpus.mac_morpho.words()
corpus_tags = nltk.corpus.mac_morpho.tagged_sents() # doctest: +NORMALIZE_WHITESPACE

print ("Corpus: ", corpus)
for tag in  corpus_tags[0]:
    print ("Tag: ", tag)