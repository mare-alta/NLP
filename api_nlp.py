import nltk
from nltk.stem import RSLPStemmer
from flask import Flask, request

app = Flask(__name__)

class CategorizaDream(object):
    def __init__(self, frase):
        self.frase = frase
        self.dados = self.DadosParaTreino()
        self.treino = self.Aprendizado(self.dados)
        self.resultado = self.Scoragem(sentence=self.frase)[0]

    def Aderencia(self, sentence, class_name):
        score = 0
        sentence_ajustada = self.Tokenize(sentence)
        sentence_ajustada = self.Stemming(sentence_ajustada)
        sentence_ajustada = self.RemoveStopWords(sentence_ajustada)
        for word in sentence_ajustada:
            if word in self.treino[class_name]:
                score += self.treino[class_name][word]
        return score

    def Tokenize(self, sentence):
        sentence_ajustada = sentence.lower()
        sentence_ajustada = nltk.word_tokenize(sentence_ajustada)
        return sentence_ajustada

    def Stemming(self, sentence):
        stemmer = RSLPStemmer()
        phrase = []
        for word in sentence:
            phrase.append(stemmer.stem(word.lower()))
        return phrase

    def RemoveStopWords(self, sentence):
        stopwords = nltk.corpus.stopwords.words('portuguese')
        phrase = []
        for word in sentence:
            if word not in stopwords:
                phrase.append(word)
        return phrase

    def DadosParaTreino(self):
        '''DADOS DE TREINAMENTO'''
        training_data = []
        training_data.append({"classe": "Alto", "frase": "Houve um derramamento de óleo"})
        training_data.append({"classe": "Alto", "frase": "Aconteceu uma explosão"})
        training_data.append({"classe": "Alto", "frase": "Ta pegando fogo"})
        training_data.append({"classe": "Alto", "frase": "O navio ta afundando"})
        training_data.append({"classe": "Alto", "frase": "O guindaste caiu"})
        training_data.append({"classe": "Alto", "frase": "Vazamento tóxico"})
        training_data.append({"classe": "Médio", "frase": "Congestionamento de caminhões"})
        training_data.append({"classe": "Médio", "frase": "Navio em estado ruim"})
        training_data.append({"classe": "Médio", "frase": "Falta de inspeção"})
        training_data.append({"classe": "Médio", "frase": "Aparelho com defeito"})
        training_data.append({"classe": "Médio", "frase": "Derramamento de líquido no chão"})
        training_data.append({"classe": "Médio", "frase": "Container não está encaixado"})
        training_data.append({"classe": "Baixo", "frase": "Banheiro ta estragado"})
        training_data.append({"classe": "Baixo", "frase": "Não tem mais água"})
        training_data.append({"classe": "Baixo", "frase": "Ta muito quente"})
        training_data.append({"classe": "Baixo", "frase": "Ar condicionado não ta funcionando"})
        training_data.append({"classe": "Baixo", "frase": "Container ta sujo"})
        training_data.append({"classe": "Baixo", "frase": "Chão ta escorregando"})
        print("%s frases incluidas" % len(training_data))
        return training_data

    def Aprendizado(self, training_data):
        corpus_words = {}
        for data in training_data:
            frase = data['frase']
            frase = self.Tokenize(frase)
            frase = self.Stemming(frase)
            frase = self.RemoveStopWords(frase)
            class_name = data['classe']
            if class_name not in list(corpus_words.keys()):
                corpus_words[class_name] = {}
            for word in frase:
                if word not in list(corpus_words[class_name].keys()):
                    corpus_words[class_name][word] = 1
                else:
                    corpus_words[class_name][word] += 1
        return corpus_words

    def Scoragem(self, sentence):
        '''DEFINE O GRUPO'''
        high_score = 0
        classname = 'Outros'
        for classe in self.treino.keys():
            pontos = 0
            pontos = self.Aderencia(sentence, classe)
            if pontos > high_score:
                high_score = pontos
                classname = classe
        return classname, high_score

@app.route('/gravidade', methods=['POST'])
def gravidade():
    data = request.get_json()["texto"]
    test = CategorizaDream(frase=data)
    return test.resultado

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)