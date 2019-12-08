# Repositório de Processamento de Linguagem Natural

Modelo usado para classificação de gravidade de textos ao serem inseridos no banco de dados

## Instalação

```bash
pip3 install Flask
pip3 install nltk
```

## Uso

```python
python3 api_nlp.py
```

## Api
A api está online no endereço [http://willianchan.pythonanywhere.com/gravidade](http://willianchan.pythonanywhere.com/gravidade)

para utilizá-la basta enviar uma requisição POST com body exemplo a seguir no formato json

```python
{"texto":"ônibus pegando fogo"}
```

# API para classificação de imagens inapropriadas

também foi desenvolvido um modelo de machine learning capaz de identificar se uma imagem é inapropriada ou não para o envio de uma reclamação.

É fornecido uma collection do postman para realizar teste da api.

[postman collection](./filtro.postman_collection.json)

A api está hospedada em [https://177.67.49.218/powerai-vision-ingram/api/dlapis/ab043177-91a0-4727-8f42-f77a282a13b9](https://177.67.49.218/powerai-vision-ingram/api/dlapis/ab043177-91a0-4727-8f42-f77a282a13b9)

É necessário enviar requisição POST com form-data com imagem

![WhatsApp Image 2019-12-08 at 08 42 02](https://user-images.githubusercontent.com/36850947/70389116-b07e9d80-1999-11ea-922d-76beb8a79660.jpeg)

![WhatsApp Image 2019-12-08 at 08 43 35](https://user-images.githubusercontent.com/36850947/70389114-a52b7200-1999-11ea-82c0-404ae7a8c5a1.jpeg)
