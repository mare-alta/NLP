import spacy

import warnings
warnings.filterwarnings("ignore")

nlp = spacy.load('pt')

doc = nlp(u'Eu gostaria de denunciar um abuso sexual.')

graus = {"grave":{"tokens":["morte","enchente"," derramamento","incêndio"], "grau": 0},"medio":{"tokens":["abuso", "estupro"],"grau":0}}

tokens = [token for token in doc]

for token in tokens:
    for key in graus:
        for palavra in graus[key]["tokens"]:
            similaridade = token.similarity(nlp(palavra))
            if similaridade > graus[key]["grau"]:
                graus[key]["grau"] = similaridade

if graus["grave"]["grau"] >= graus["medio"]["grau"]:
    print("ocorrência é grave")
elif graus["medio"]["grau"] > 0.1:
    print("ocorrência é média")
else:
    print("ocorrência é leve")