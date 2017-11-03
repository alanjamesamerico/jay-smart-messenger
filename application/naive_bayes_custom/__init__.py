from nltk.tokenize import word_tokenize

_LANGUAGE   = "portuguese"

'''
Analisar o porquê que a probabilidade maior é pra quem 
está com um menor número de classes na base de treinamento.

'''

___TRAIN_SET__ = [
('Meu pai é o melhor', 'BOA'),
('Pessoas legais são pessoas boas!', 'BOA'),
('Este é um lugar incrível!', 'BOA'),
#("Eu me sinto muito bem com essas crianças.", "BOA"),
('Este é o meu melhor trabalho.', 'BOA'),
("Briguei com minha namorada", "RUIM"),
#('Você está com dor de cabeça', 'RUIM'),
#('Nunca mais falo com você', 'RUIM'),
('Estou irado!', 'RUIM'),
#('Não como neste restaurante', 'RUIM'),
#('até que esse lache é bom', 'MODERADO'),
('o tempo está nublado', 'MODERADO'),
('acho que eu vou', 'MODERADO')]

# CUSTOM
__TRAIN_SET__ = [
#("Não deixe de tirar fotos na réplica do 14 Bis e do Bandeirante.", "parqSantosDumont"),
#("Parque muito gostoso, bem localizado, bem arborizado e bem cuidado", "parqSantosDumont"),
#("Wifi gratis, tranqüilidade, segurança e paz bem no centro da cidade, fica lotado aos domingos.", "parqSantosDumont"),
#("Tem um jardim japonês lindo.", "parqSantosDumont"),
#("Lugar bom pra levar as crianças. Tem parquinho, chafariz, banheiros e até quiosque com pontos de tomadas.", "parqSantosDumont"),
#("Bem tranquilo, com alguns aviões e um lago com peixes enormes!", "parqSantosDumont"),
("Local bom pra praticar esportes, correr, se exercitar e até passear com a família ou namorada", "parqSantosDumont"),
("Um ótimo lugar para passar o dia conversando e se divertindo com os amigos e familiares", "parqSantosDumont"),
("Simplesmente lindo e aconchegante. Lugar ótimo pra relaxar depois de um dia de trabalho.", "parqSantosDumont"),
("Muito bom para crianças e adultos que querem passar um momento com a família.", "parqSantosDumont"),
("Adoro esse lugar! Excepcional para um passeio de fim de semana!", "parqSantosDumont"),
("Lugar incrível para caminhar, correr e exercitar-se", "parqSantosDumont"),
("Muito bom para curtir com os amigos, e tem wifi grátis", "parqSantosDumont"),
("Caminhar aqui é uma delicia - segurança, conforto e muita gente.", "parqSantosDumont"),
  
#("Ótimo lugar para se divertir e fazer exercícios.", "parqCidade"),
#("Bom lugar para pedalar", "parqCidade"),
#("Ótimo lugar para se passar com a família!", "parqCidade"),
#("Ótimo lugar pra fazer picnic, andar de bike, descansar perto do lago. Muito arborizado. ", "parqCidade"),
#("Ótimo lugar para estar com a família", "parqCidade"),
#("Lugar muito bonito para fotografia!", "parqCidade"),
#("Amo o paisagismo e suas palmeiras imperiais! Maravilhoso!", "parqCidade"),
#("Muito bom para passear com a família. As crianças adoram andar de bicicleta", "parqCidade"),
#("Além do lazer em geral, muito bom para avistar, fotografar aves, pra quem gosta o parque tem uma boa avifauna!", "parqCidade"),
#("Paisagismo maravilhoso! O parque é enorme", "parqCidade"),
("Lindo parque, tem esquilos,capivara. Bem arborizado, ótimo para relaxar e ler um bom livro", "parqCidade"),
("um lugar top, com muita árvore formando um paisagismo muito bonito. Recomendo!", "parqCidade"),
("Lugar lindo parece o paraíso ! Recomendo trás paz", "parqCidade"),
("Ótimo para namorar, fazer piquenique e refletir sobre a vida!", "parqCidade"),
("Um bom lugar para andar de bicicleta", "parqCidade"),
   
#("O melhor parque da cidade, sempre tem eventos, o melhor é o cinema ao ar livre.", "parqVicenAranha"),
#("Lugar muito bom, bastante arborizado, com eventos diversos toda semana. ", "parqVicenAranha"),
#("Espaçoso e cheio de atrações culturais e gastronômicas nos finais de semana", "parqVicenAranha"),
#("Muito bom pra passear, curtir, descansar e meditar. Ótimo pra levar a família.", "parqVicenAranha"),
#("Um dos melhores parques da região! Sempre tem eventos muito legais. Amo!", "parqVicenAranha"),
#("Local muito agradável para caminhada", "parqVicenAranha"),
("Um dos melhores lugares para praticar corrida", "parqVicenAranha"),
("Ótimo pra caminhadas e corridas e aos domingos show ao ar livre", "parqVicenAranha"),
("Fique atendo a programação cultural do parque, sempre tem algo muito bom", "parqVicenAranha"),
("Ótimo lugar para fazer caminhadas e relaxar contemplando a paisagem", "parqVicenAranha"),
("Música ao vivo aos finais de semana e um clima muito agradável.", "parqVicenAranha"),
("Um belo lugar para passear e se distrair", "parqVicenAranha"),

#("Ótimo lugar para um lanche rápido", "mercadao"),
#("Tem de tudo, mas eu vou comer pastel. Um melhor que o outro", "mercadao"),
#("As pastelarias são ótimas", "mercadao"),
#("Gosto de ir só para comer pastel", "mercadao"),
#("Vale apena. Muito gostoso", "mercadao"),
#("Pastel do Sergio é o melhor e mais antigo do", "mercadao"),
("Bom lugar para comer", "mercadao"),
("Baraca da Rebeca alem da simpatia da Dona, os doces são uma delicia.", "mercadao"),
("Melhor pastel da cidade", "mercadao"),
("Ir ao mercado e comer um pastel de carne acompanhado de uma caçulinha é fundamental", "mercadao"),

#("Lugar onde guarda um pouco da história do Departamento de Ciência e Tecnologia Aeroespacial e do ITA - Instituto Tecnológico de Aeronáutica", "mab"),
("o cta é um bom lugar pra visitar", "mab"),
("Lugar excelente para vir com a família e conhecer um pouco sobre a história da aviação", "mab"),
("Muito bacana! História, miniaturas e fotos. Vale a visita", "mab"),
("O Memorial traz um pouco da história aeroespacial do Brasil, como foguetes, aviões de caça, e um dos primeiros aparelhos de fax", "mab"),
("Localizado no Centro Técnico Aeroespacial CTA", "mab")
]


'''    
("Lugar que nos liga ao céu. Oração e meditação", "igrejaMatriz"),
("Lugar de devoção", "igrejaMatriz"),
("Igreja que convida à oração, quietude e paz", "igrejaMatriz"),
    
("Tem uma vista muito bonita nos fins de tarde!", "miranteBanhado"),
("Lindo pôr do sol", "miranteBanhado"),
("Bela vista pela manhã.", "miranteBanhado"),
("Cartão postal da cidade com o pôr do sol mais lindo.", "miranteBanhado"),
("Não deixe de contemplar o por do sol neste local, fenomenal.", "miranteBanhado"),
("Lugar lindo para caminhar e apreciar o por do sol.", "miranteBanhado"),
("Melhor pôr-do-sol de todos os lugares que eu já fui", "miranteBanhado"),
("Uma bela vista de São José dos Campos, que é uma das marcas registradas da cidade.", "miranteBanhado"),
("Vista magnífica, ótimo pra relaxar e caminhar.", "miranteBanhado"),
("Uma das melhores vistas da cidade", "miranteBanhado"),
    
("Lugar excelente para vir com a família e conhecer um pouco sobre a história da aviação", "mab"),
("Muito bacana! História, miniaturas e fotos. Vale a visita", "mab"),
("O Memorial traz um pouco da história aeroespacial do Brasil, como foguetes, aviões de caça, e um dos primeiros aparelhos de fax", "mab"),
("Lugar onde guarda um pouco da história do Departamento de Ciência e Tecnologia Aeroespacial e do ITA - Instituto Tecnológico de Aeronáutica", "mab"),
("Localizado no Centro Técnico Aeroespacial CTA", "mab"),
    
("Linda paisagem de águas limpas e calma", "repJaguari"),
("Visual muito agradável ao final da tarde e ao amanhecer, muita vegetaçao", "repJaguari"),
("Local ideal para quem quer tranquilidade e adora natureza, passar com a família", "repJaguari"),
("Excelente passeio onde você pode fazer passeio de lancha, desfrutar de um banho nas águas da represa e saborear as comidas dos restaurantes", "repJaguari"),
("Bom lugar para nadar", "repJaguari"),
("Local agradável para navegar e remar ", "repJaguari"),
("Águas tranguilas para passear de caiaque e standup ", "repJaguari"),
("Ótimo local para a prática de esportes, aproveite para fazer um pic nic e aproveitar o dia com as crianças.", "repJaguari"),
("Um ótimo local para a pratica de esportes como a canoagem e a pesca esportiva, vale a pena conferir", "repJaguari"),
("Excelente para levar a família aos finais de semana, montar uma barraca e fazer um churrasco ou piquenique", "repJaguari"),
("Um bom local para nadar", "repJaguari"),
("Bom para andar de barco e jet ski", "repJaguari"),
    
("O jardim é pequeno, mas bonito. Um lugar tranquilo, que rende belas fotos", "torii"),
("Um bom lugar para tirar fotos e bem bonito e limpo , bem calmo com bancos e flores, fácil de estacionar", "torii"),
("Um ótimo lugar para quem gosta de paisagismo e caminhadas", "torii"),
("Jardim Japonês Tipico muito bonito e sempre bem conservado pela colonia japonesa de São José dos Campos", "torii"),
("Excelente local para caminhada, levar as crianças para passear, e andar ao ar livre. ", "torii"),
    
("Um lugar onde se revive a arte sacra por peças genialmente confeccionadas por artesões da região.", "arteSacra"),
("Exposição organizada, local limpo, profissionais qualificados na recepção dos visitantes.", "arteSacra"),
("Peças históricas que contam um pouco da história religiosa e aspectos sacros de São José dos Campos", "arteSacra"),
("Pode-se ver esculturas, quadros de cerâmica e você pode fotografar tudo. Vale a pena a visita", "arteSacra"),
("Linda construção. Pequeno mas muito bem cuidado. Vale a pena conhecer.", "arteSacra")
'''


_LEXICON  = set(word.lower() for passage in __TRAIN_SET__ for word in word_tokenize(passage[0], _LANGUAGE))
#print("\n\t LEXICO: %s" %_LEXICON)

__TEST_TRAIN__ = [
("A cerveja era boa.", "BOA"),
('Não gosto do meu trabalho', 'RUIM'),
("Eu não estou me sentindo dândi hoje.", "RUIM"),
("Eu me sinto incrível!", "BOA"),
('Gary é um amigo meu', 'BOA'),
("Talvez eu vá.", "MODERADO"),
("Não sei se eu consigo ir para sua festa hoje", "MODERADO")]



