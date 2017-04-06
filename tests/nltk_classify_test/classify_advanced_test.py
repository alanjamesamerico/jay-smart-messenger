#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nltk
from nltk.tokenize import word_tokenize
from itertools import chain
'''
training_data = [
('I love this sandwich.', 'pos'),
('This is an amazing place!', 'pos'),
('I feel very good about these beers.', 'pos'),
('This is my best work.', 'pos'),
("What an awesome view", 'pos'),
('I do not like this restaurant', 'neg'),
('I am tired of this stuff.', 'neg'),
("I can't deal with this", 'neg'),
('He is my sworn enemy!', 'neg'),
('My boss is horrible.', 'neg')]
'''

training_data = [
('Eu amo este sanduíche.', 'Pos'),
('Meu pai é o melhor', 'Pos'),
('Pessoas leguais são pessoas boas!', 'Pos'),
('Este é um lugar incrível!', 'Pos'),
("Eu me sinto muito bem com essas cervejas.", "Pos"),
('Este é o meu melhor trabalho.', 'Pos'),
("Que visão fantástica", "pos"),
('Não como este restaurante', 'neg'),
("Estou cansado dessas coisas.", "Neg"),
("Eu não posso lidar com isso", "neg"),
("Ele é meu inimigo jurado!", "Neg"),
("Aquela música é ruim", "Neg"),
("Não gosto de ouvir você!", "Neg"),
('Meu chefe é horrível.', 'Neg')]

phrase = word_tokenize('I love this sandwich.'.lower())
print("Sentence Tokenize: %s" %phrase)

vocabulary = set(chain(*[word_tokenize(i[0].lower(), 'portuguese') for i in training_data])) # all words
x =  {i:True for i in vocabulary if i in phrase}
y =  {i:False for i in vocabulary if i not in phrase}
print("\nVOCABYLARY: %s" %vocabulary, "\nVOCABYLARY e PHRASE: %s" %x, "\nVOCABYLARY e não na PHRASE: %s" %y, "\nX update: %s" %x.update(y))

feature_set = [({i:(i in word_tokenize(sentence.lower(), 'portuguese')) for i in vocabulary},tag) for sentence, tag in training_data]
#print("\n\nFeature Set: %s" %feature_set)

classifier = nltk.NaiveBayesClassifier.train(feature_set);

test_sentence = "eu sou feliz aqui"
featurized_test_sentence =  {i:(i in word_tokenize(test_sentence.lower(), 'portuguese')) for i in vocabulary}

print("\nClassification: %s" %classifier.classify(featurized_test_sentence), "\nAccuracy: %.4f" %nltk.classify.accuracy(classifier, feature_set))

print("\n\n### end train ###")