# Feira da Fruta

[![Feira da Fruta](http://i.vimeocdn.com/video/507837882_1280x720.jpg)](https://youtu.be/4pcJSn791IE)


Teste do servidor:

```sh
while $(sleep 2); do time curl //$ENDPOINT/; done
```


### Migração do banco de dados

[Documentação do Flask-Migrate](http://flask-migrate.readthedocs.io/en/latest/)
[Documentação do Flask SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/)


> Para iniciar o projeto de banco de dados use o comando de `init`:
```sh
$ python manage.py db init
```

> Para gerar os statements e metadados de migração usamos o `migrate` como abaixo:
```sh
$ python manage.py db migrate
```

> Para commitar as alterações no banco de dado usamos o comando de `upgrade`:
```sh
$ python manage.py db upgrade
```

> Se precisar de ajuda use a opção de `--help`

```sh
$ python manage.py db --help
```
