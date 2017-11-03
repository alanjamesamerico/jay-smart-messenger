'''
Created on 5 de mai de 2017

@author: Alan James
'''
from application.naive_bayes_custom.naive_bayes_custom  import NaiveBayesCustom
from application.naive_bayes_custom.processing_text     import ProcessingText
from application.naive_bayes_custom.pre_processing_text import PreProcessingText


nb = NaiveBayesCustom()
pt = ProcessingText()
prePt = PreProcessingText()
__number_class__ = 5

'''
"sabe o que eu queria? Bom, era poder caminhar em um lugar lindo!",
"quero ir hoje conhecer o CTA",
"QuERO iR hoje Conhecer o cta",
"to afim de um pastel",
"gostaria de comer",
"quero sair com os meus familiares" ,
"quero curtir uma bom evento com música ao vivo",
"quero andar de bicicleta",
"queria conhecer algum lugar de são josé, onde posso ir?",
"Qual é o lugar mais lindo dessa cidade?",
"gostaria de ir em um lugar lindo de são josé?",
"quero levar minha família para passear",
"dizem que o cta é um bom lugar pra visitar",
"onde tem show ao vivo?",
"quero ir em um lugar onde tem muita árvore"
'''

texts = [
"quero ir pra um lugar onde dê pra praticar algum esporte",
"gostaria de ir em um lugar histórico",
"quero visitar o lugar mais antigo de são josé",
"desejo correr",
"quero levar meu filho pra sair!"
]

'''
    ####################################
    #    PROCESSAMENTO DO TEST SET    #
    ####################################
'''
    
def processNBNative(text):
    nb.train()
    nb.test(text)
    showClassification(nb)
    
def processNBCustom(text):
    text = pt.applyTokenizer(text)
    text = pt.applyRemovalStopwordsByList(text)
    text = pt.cleanText(text)
    text = pt.lowerCase(text)
    
    prePt.applyRemovalStopwordsPreTrainSet()
    trainSet = prePt.applyCleanSentencesTrainSet()
    nb.trainCustom(trainSet)
    nb.test(text)
    showClassification(nb)
    
def showClassification(classifier):
    print(classifier.getClassification())
    #print(">> Accuracy \t\t- %.4f" %classifier.getAccuracy())
    probLabels = classifier.getProbabilityAllClasses()
    for i in range(__number_class__):
        j = 0
        print("%s" %probLabels[i][j+1])

if __name__ == '__main__':
    
    for i in range(len(texts)):
        print(texts[i])
        processNBNative(texts[i])
        processNBCustom(texts[i])
        print("\n---\n")