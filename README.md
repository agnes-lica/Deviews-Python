# M5 - Deviews

## Objetivo

Consiste no projeto final do M5, onde o objetivo é criar o backend de uma rede social para desenvolvedores.

## Comandos uteis

1. Para ativar o `venv`

```shell
source venv/bin/activate
```

2. Para fazer a instalações dos pacotes

```shell
pip install -r requirements.txt
```

3. Ao realizar qualquer instalação de um novo pacote realizar o comando

```shell
pip freeze>requirements.txt
```

4. Para fazer migrations

```shell
python manage.py makemigrations
```

```shell
python manage.py migrate
```

5. Para rodar o servidor

```shell
python manage.py runserver
```

6. Para criar apps

```shell
python manage.py startapp `nome do pacote`
```
