# Flask-Producao-Gunicorn-WSGI
Rodando flask em ambiente de producao wsgi com gunicorn

O arquivo que contem a aplicacao flask é o app_production_wsgi.py só que em vez de chama-lo direto via python iremos utilizar o gunicorn.

Para instalar o gunicorn:

sudo apt-get install gunicorn

Depois de instalado só rodar o arquivo wsgi.py que faz referencia ao app_production_wsgi.py da seguinte maneira:

gunicorn --bind 127.0.0.1:8081 wsgi:app

Ou tambem a opcao de chamar direto o arquivo app_production_wsgi.py sem usar o wsgi.py e com 4 Workers por exemplo da seguinte maneira:

gunicorn --bind 127.0.0.1:8081 -w 4 app_production_wsgi:app

