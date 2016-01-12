# Pratica do curso WTTD 

Curso ministrado pelo Henrrique Bastos

[![Build Status](https://travis-ci.org/pulidog/eventex.svg?branch=master)](https://travis-ci.org/pulidog/eventex)
[![Code Health](https://landscape.io/github/pulidog/eventex/master/landscape.svg?style=flat)](https://landscape.io/github/pulidog/eventex/master)

# Contexto

Um cliente liga e pede para fazer um sistema de inscrições 'URGENTE', para un evento chamado de 'EVENTEX',
 ai agente pega o projeto e tenta fazer ...


# EVENTEX

sistema de eventos encomendado pela Morena

## Como desenvolver?

1. Clone o repositorio.
2. Crie un virtualenv com python 3.5.
3. Ative o virtualenv.
4. Instale as dependencias.
5. Configure a instancia com o .env.
6. Execute os testes.

```console
git clone git@github.com/pulidog/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie um instancia no heroku.
2. Envie as configurações para heroku.
3. Define uma Secret_Key para instancia.
4. Defina DEBUG=False.
5. Configure o serviço de email.
6. envie o codigo para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# Configurar o email
git push heroku master --force

```