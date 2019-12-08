# Repositório de Processamento de Linguagem Natural

Modelo usado para classificação de gravidade de textos ao serem inseridos no banco de dados

## Instação

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip3 install flask
pip3 install nltk
```

## Uso

```python
python3 api_nlp.py
```

# Api
A api está online no endereço [http://willianchan.pythonanywhere.com/gravidade](http://willianchan.pythonanywhere.com/gravidade)

para utilizá-la basta enviar uma requisição POST com body exemplo a seguir no formato json

```python
{"texto":"ônibus pegando fogo"}
```
