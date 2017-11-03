'''
Created on 5 de mai de 2017

@author: Alan James
'''
from application.naive_bayes_custom.naive_bayes_custom import NaiveBayesCustom
from application.naive_bayes_custom.processing_text import ProcessingText
from application.naive_bayes_custom.pre_processing_text import PreProcessingText


nb = NaiveBayesCustom()
pt = ProcessingText()
prePt = PreProcessingText()
__number_class__ = 5

#text = "você não vai gostar disso"                    # RUIM
#text = "acho que você poderia fazer isso pra mim"     # MODERADO
#text = "hoje o dia está maravilhoso"                  # BOA

#text = "quero andar de bicicleta"                 # Parque da Cidade 
#text = "quero curtir uma bom evento com música ao vivo"                  # Vicentina
#text = "quero sair com os meus familiares"        # Parque Santos Dumont
#text = "gostaria de comer"                      # Mercado
#text = "to afim de um pastel"                      # Mercado
#text = "QuERO iR hoje Conhecer o cta"
#text = "quero ir hoje conhecer o CTA" # case sencitive
#text = "sabe o que eu queria? Bom, era poder caminhar em um lugar lindo!"
#text = "queria conhecer são josé, onde posso ir?"
#text = "queria conhecer são josé, onde posso ir? quero levar minha família para passear"

#text = "queria conhecer são josé, onde posso ir?"
#text = "quero levar minha família para passear"
#text = "quero conhecer o CTA"
#text = "onde tem show ao vivo?"
#text = "quero ir em um lugar onde tem muita árvore"
#text= "queria conhecer algum lugar de são josé, onde posso ir?"
#text = "Qual é o lugar mais lindo dessa cidade?"
text = "gostaria de ir em um lugar lindo de são josé?"
print("----\nText: %s\n----" %text)


'''
    ####################################
    #    PROCESSAMENTO DO TEST SET    #
    ####################################
'''
    
def processNBNative(text):
    print("\n# TEXTO SEM PROCESSAR\n#####################")
    #prePt.applyRemovalStopwordsPreTrainSet()
    nb.train()
    nb.test(text)
    showClassification(nb)
    
def processNBCustom(text):
    print("\n# TEXTO PROCESSADO\n###################")
    text = pt.applyTokenizer(text)
    #print("\n\t\tLower: ", text)
    text = pt.applyRemovalStopwordsByList(text)
    text = pt.cleanText(text)
    text = pt.lowerCase(text)
    #print("Text clean: ", text)
    #text = pt.applyStemmersByList(text)
    
    #trainSet =prePt.applyRemovalStopwordsPreTrainSet()
    trainSet = prePt.applyCleanSentencesTrainSet()
    nb.trainCustom(trainSet)
    #nb.train()
    print (">texto processado: ", text)
    nb.test(text)
    showClassification(nb)
    
def showClassification(classifier):
    print("\n>> Classification MAX \t- %s" %classifier.getClassification())
    print(">> Accuracy \t\t- %.4f" %classifier.getAccuracy())
    probLabels = classifier.getProbabilityAllClasses()
    for i in range(__number_class__):
        j = 0
        print("\n* Probabiliteis - %s | %s" %(probLabels[i][j], probLabels[i][j+1]))

if __name__ == '__main__':
    processNBNative(text)
    processNBCustom(text)
    

















    
    
'''
    ####################################
    #    PROCESSAMENTO DO TRAIN SET    #
    ####################################
    
    #text = "Hmm isso é muito bom, e se possível eu gostaria de falar pra todos!" # BOA
    #text = "será que isso vai dar certo" # MODERADA
    #text = "Hmm isso é muito bom, e se possível eu gostaria de falar pra todos!" # RUIM
    
    #text = "você não vai gostar disso"                    # RUIM
    #text = "acho que você poderia fazer isso pra mim"     # MODERADO
    text = "hoje o dia está maravilhoso"                  # BOA
    
    print("----\nText: %s\n----" %text)
    
    print("\n# TEXTO NÃO PROCESSADO e TRAIN SET PROCESSADO\n##############################################")
    
    preProcessTrain = nb.preProcessingTrain()
    nb.trainCustom(preProcessTrain)
    nb.test(text)
    
    print("\n>> Classification MAX - \t%s" %nb.getClassification())
    print(">> Accuracy - \t\t\t%.4f" %nb.getAccuracy())
    probLabels = nb.getProbabilityAllClasses()
    #print(">> Probabiliteis - \t\t%s: %s | %s: %s" %(probLabels[0][0], probLabels[0][1], probLabels[1][0], probLabels[1][1]))
    print("\n>> Probabiliteis - %s: %s | %s: %s | %s: %s" %(probLabels[0][0], 
                                                              probLabels[0][1], 
                                                              probLabels[1][0], 
                                                              probLabels[1][1], 
                                                              probLabels[2][0], 
                                                              probLabels[2][1]))
    
    
   
    print("\n\n# TEXTO PROCESSADO e TRAIN SET PROCESSADO\n##############################################")
    
    preProcessTrain = nb.preProcessingTrain()
    nb.trainCustom(preProcessTrain)
    
    text = pt.applyTokenizer(text)
    #text = pt.cleanText(text) Arrumar esse método, pois está dando erro.
    text = pt.applyRemovalStopwordsByList(text)
    text = pt.applyStemmersByList(text)
    nb.test(text)
    print("\n>> Classification MAX - \t%s" %nb.getClassification())
    print(">> Accuracy - \t\t\t%.4f" %nb.getAccuracy())
    probLabels = nb.getProbabilityAllClasses()
    print("\n>> Probabiliteis - %s: %s | %s: %s | %s: %s" %(probLabels[0][0], 
                                                              probLabels[0][1], 
                                                              probLabels[1][0], 
                                                              probLabels[1][1], 
                                                              probLabels[2][0], 
                                                              probLabels[2][1]))
    
    
    testTrain = "Eu não gosto muito quando chove. Acho horrível!"
    
    print("#################################\n#\tNaive Bayes Custom \t#\n#################################\n")
    
    #nb.train()
    nb.test(testTrain)
    print("\n----\nText: %s\n----" %testTrain)
    print("\n>> Classification MAX - \t%s" %nb.getClassification())
    print(">> Accuracy - \t\t\t%.4f" %nb.getAccuracy())
    
    probLabels = nb.getProbabilityAllClasses()
    print(">> Probabiliteis - \t\t%s: %s | %s: %s" %(probLabels[0][0], probLabels[0][1], probLabels[1][0], probLabels[1][1]))
    
    
    def processTestSetAndTrainSet():
    text = "Hmm isso é muito bom, e se possível eu gostaria de falar pra todos!"
    print("\n\n# TEXTO PROCESSADO e TRAIN SET PROCESSADO")
    preProcessTrain = nb.preProcessingTrain()
    nb.trainCustom(preProcessTrain)
    text = pt.applyTokenizer(text)
    text = pt.cleanText(text)
    text = pt.applyRemovalStopwordsByList(text)
    text = pt.applyStemmersByList(text)
    nb.test(text)
    print("\n>> Classification MAX - \t%s" %nb.getClassification())
    print(">> Accuracy - \t\t\t%.4f" %nb.getAccuracy())
    probLabels = nb.getProbabilityAllClasses()
    print(">> Probabiliteis - \t\t%s: %s | %s: %s" %(probLabels[0][0], probLabels[0][1], probLabels[1][0], probLabels[1][1]))
    return probLabels
    
def noProcessTestSetAndProcessTrainSet():
    text = "Hmm isso é muito bom, e se possível eu gostaria de falar pra todos!"
    print("\n# TEXTO NÃO PROCESSADO e TRAIN SET PROCESSADO")
    preProcessTrain = nb.preProcessingTrain()
    nb.trainCustom(preProcessTrain)
    nb.test(text)
    #print("\n>> Classification MAX - \t%s" %nb.getClassification())
    #print(">> Accuracy - \t\t\t%.4f" %nb.getAccuracy())
    probLabels = nb.getProbabilityAllClasses()
    #print(">> Probabiliteis - \t\t%s: %s | %s: %s" %(probLabels[0][0], probLabels[0][1], probLabels[1][0], probLabels[1][1]))
    return probLabels

    
    '''

    
'''
    count = 0
    soma1 = 0
    soma2 = 0
    for i in range(0,99):
        probLabels = processTestSetAndTrainSet()
        prob1 = float(probLabels[0][1])
        soma1 = soma1 + prob1
        prob2 = float(probLabels[1][1])
        soma2 = soma2 + prob2
        count = count + 1
    print("\nIterações: ", count)
    print("\n# Média da probabilidade\nBOA: %f\nRUIM: %f" %((soma1/count),(soma2/count)))
    print("\n# Porcentagem de acerto: \nBOA: %.2f\nRUIM: %.2f" %((soma1/count)*100,(soma2/count)*100))
    
    '''
'''
    count = 0
    soma1 = 0
    soma2 = 0
    for i in range(0,99):
        probLabels = noProcessTestSetAndProcessTrainSet()
        prob1 = float(probLabels[0][1])
        soma1 = soma1 + prob1
        prob2 = float(probLabels[1][1])
        soma2 = soma2 + prob2
        count = count + 1
    print("\nIterações: ", count)
    print("\n# Média da probabilidade\nBOA: %f\nRUIM: %f" %((soma1/count),(soma2/count)))
    print("\n# Porcentagem de acerto: \nBOA: %.2f\nRUIM: %.2f" %((soma1/count)*100,(soma2/count)*100))
    '''
