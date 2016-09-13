# -*- coding: utf-8 -*
# Adapted from: github.com/aneesha/RAKE/rake.py
from __future__ import division

import operator
import string

import nltk
from nltk.probability import FreqDist
from nltk.corpus import floresta
from nltk.corpus import mac_morpho
from nltk.corpus import floresta
from nltk.stem import RSLPStemmer

_tags_florest    = floresta.tagged_words()

def isPunct(word):
    return len(word) == 1 and word in string.punctuation

def isNumeric(word):
    try:
        float(word) if '.' in word else int(word) 
        return True
    except ValueError:
        return False
    
def remove_break_line_for_archive(archive):
    lines = []
    for line in archive:
        lines.append(line.replace("\n",""))
    return lines

class RakeKeywordExtractor:

  def __init__(self):
    #archive = open ('C:\\Users\\alan.james\\Desktop\\wordsMM.txt', 'r')
    #archive = open ('C:\\Users\\alan.james\\Desktop\\wordsFlorest.txt', 'r')
    #self.stopwords = set(remove_break_line_for_archive(archive))
    self.stopwords = set(nltk.corpus.stopwords.words('portuguese'))  # stopwords.words('portuguese')
    #archive.close
    self.top_fraction = 1  # consider top third candidate keywords by score

  def _generate_candidate_keywords(self, sentences):
    phrase_list = []
    for sentence in sentences:
      words = map(lambda x: "|" if x in self.stopwords else x,
        nltk.word_tokenize(sentence.lower(), language='portuguese'))
      phrase = []
      for word in words:
        if word == "|" or isPunct(word):
          if len(phrase) > 0:
            phrase_list.append(phrase)
            phrase = []
        else:
          phrase.append(word)
    return phrase_list

  def _calculate_word_scores(self, phrase_list):
    word_freq = nltk.FreqDist()
    word_degree = nltk.FreqDist()
    for phrase in phrase_list:
      f = list(filter(lambda x: not isNumeric(x), phrase))
      degree = len(f) - 1
      for word in phrase:
        word_freq[word] =+ 1
        word_degree[word] =+ degree # word_degree.inc(word, degree)  # other words word_degree[word] =+ degree
    for word in word_freq.keys():
      word_degree[word] = word_degree[word] + word_freq[word]  # itself
    # word score = deg(w) / freq(w)
    word_scores = {}
    for word in word_freq.keys():
      word_scores[word] = word_degree[word] / word_freq[word]
    return word_scores

  def _calculate_phrase_scores(self, phrase_list, word_scores):
    phrase_scores = {}
    for phrase in phrase_list:
      phrase_score = 0
      for word in phrase:
        phrase_score += word_scores[word]
      phrase_scores[" ".join(phrase)] = phrase_score
    return phrase_scores
    
  def extract(self, text, incl_scores=False):
    sentences = nltk.sent_tokenize(self._check_final_simbol(text), language='portuguese')  # nltk.data.load('tokenizers/punkt/portuguese.pickle')
    phrase_list = self._generate_candidate_keywords(sentences)
    # Verificar o tamanho das frases e tratar as frases que conter uma tupla menor ou igual a 3
    word_scores = self._calculate_word_scores(phrase_list)
    phrase_scores = self._calculate_phrase_scores(phrase_list, word_scores)
    sorted_phrase_scores = sorted(phrase_scores.items(), key=operator.itemgetter(1), reverse=True)
    n_phrases = len(sorted_phrase_scores)
    if incl_scores:
      return sorted_phrase_scores[0:int(n_phrases / self.top_fraction)]
    else:
      return map(lambda x: x[0],
        sorted_phrase_scores[0:int(n_phrases / self.top_fraction)])
    
  def _check_final_simbol(self, text):
    if '.!?' not in text[len(text)-1]:
        return text + '.'
    else:
        return text

def check_class_grammatical(text):
    words = nltk.word_tokenize(text)
    text_tags = []
    for word in words:
        for tag in _tags_florest:
            if word in tag:
                text_tags.append(tag)
                break
    return text_tags

def parsing_class_grammatical(text_tags):
    words = []
    for text in text_tags:
     if 'H+n' or 'P+v-inf' in text:
         words.append(text)
    return words

def tags(text):
    words = nltk.word_tokenize(text)
    for word in words:
        for tag in _tags_florest:
            if word in tag:
                print ('Word: %s \t-\ttag: %s' %(word, tag))
                break
def test():
  rake = RakeKeywordExtractor()
  
  text1 = 'Quais são os endereços das praias mais proximas?'
  text2 = 'Quais são os endereços dos hospitais mais próximos?'
  text3 = 'O Alan comeu uma maça'
  text4 = 'Como faço para comer uma comida agora'
  text5 = 'Onde eu posso comer?'
  text6 = 'Gostaria de chegar até a praia'
  text7 = 'Como faço para chegar até a minha casa?'
  text8 = 'Quais são os atrativos da semana?'
  text9 = 'Que horas será o evento xpto?'
  text10 = 'Quais os horário de atendimento?'
  text11 = 'Gostaria de comer'
  text12 = 'Quero saber mais'
  text13 = 'Quero sair'
  text14 = 'não estou bem'
  text15 = 'viajar'

  print (text1, "\n",rake.extract(text1, incl_scores=True))
  print ("\n", text2, "\n", rake.extract(text2, incl_scores=True))
  print ("\n", text3, "\n", rake.extract(text3, incl_scores=True))
  print ("\n", text4, "\n", rake.extract(text4, incl_scores=True))
  print ("\n", text5, "\n", rake.extract(text5, incl_scores=True))
  print ("\n", text6, "\n", rake.extract(text6, incl_scores=True))
  print ("\n", text7, "\n", rake.extract(text7, incl_scores=True))
  print ("\n", text8, "\n", rake.extract(text8, incl_scores=True))
  print ("\n", text9, "\n", rake.extract(text9, incl_scores=True))
  print ("\n", text10, "\n", rake.extract(text10, incl_scores=True))
  print ("\n", text11, "\n", rake.extract(text11, incl_scores=True))
  print ("\n", text12, "\n", rake.extract(text12, incl_scores=True))
  print ("\n", text13, "\n", rake.extract(text13, incl_scores=True))
  print ("\n", text14, "\n", rake.extract(text14, incl_scores=True))
  print ("\n", text15, "\n", rake.extract(text15, incl_scores=True))

# Simple case.
def test_extract_parsing_1(text1):
  rake = RakeKeywordExtractor()
  
  #text1 = 'Onde eu poderia almoçar? tem algum restaurante aqui por perto?'
  print (rake.extract(text1, incl_scores=True), "\n")
  
  list_words = rake.extract(text1, incl_scores=True)
  words_tags = []
  # Simple Case.
  if len(list_words) == 1:
       phrase = list_words[0][0]
       print ('Frase: ', phrase)
       phrase_class = check_class_grammatical(phrase)
       wt = parsing_class_grammatical(phrase_class)
       print ('\nPalavra(as) extraída(as): ', wt)
       
def test_extract_parsing_2(text1):
  rake = RakeKeywordExtractor()
  language = 'portuguese'
  #text1 = 'Onde eu poderia almoçar? tem algum restaurante aqui por perto?'
  print (rake.extract(text1, incl_scores=True), "\n")
  
  list_words = rake.extract(text1, incl_scores=True)
  words_tags = []
  
  for tuple in list_words:
      if len(nltk.word_tokenize(tuple[0], language)) == 2:
          phrase = tuple[0]
          print ('Frase: ', phrase)
          phrase_class = check_class_grammatical(phrase)
          wt = parsing_class_grammatical(phrase_class)
          for w in wt:
              words_tags.append(w)
  return words_tags

def test_whith_stemmers():
  rake = RakeKeywordExtractor()
  stemmer = RSLPStemmer()
  
  text1 = 'Eu quero comer'
  print (rake.extract(text1, incl_scores=True), "\n")
  
  list_words = rake.extract(text1, incl_scores=True)
  words_tags = test_extract_parsing_2(text1)
  for w in words_tags:
     print (w[0], '\ts/ Morfologia: ', stemmer.stem(w[0]))

if __name__ == "__main__":
    
  test()
  #print (test_extract_parsing_2(""))
  #test_whith_stemmers()