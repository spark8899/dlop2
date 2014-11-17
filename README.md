dlop
====

web ops system

Quick start
===========

> You need a MongoDB instance running locally or remotely to connect. 
> dlop runs on Python 2.6
> install virtualenv pip python-dev

0. install pip

```bash
download https://pypi.python.org/pypi/pip#downloads
# tar zxvf pip-1.5.6.tar.gz && cd pip*
# python setup.py install  #required python-setuptools
# vi ~/.pip/pip.conf
[global]
index-url=http://pypi.douban.com/simple
# pip --proxy http://proxy-server:proxy-port install virtualenv
```

1. Get dlop

```bash
# git clone https://github.com/spark8103/dlop
# cd dlop
# virtualenv flask
# flask/bin/pip install -r requirements.txt
```

2. setting Mysql 

```bash
mysql> create database dlop;
mysql> grant all on dlop.table to dlop@localhost;
mysql> set password for dlop@localhost = password('dlop');
mysql> flush privileges;

# cat config.py
import os
_basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'srr9KJ8IHElAZF869w'

MYSQL_DATABASE_USER="dlop"
MYSQL_DATABASE_PASSWORD="dlop"
MYSQL_DATABASE_DB="dlop"
MYSQL_DATABASE_HOST="localhost"

SQLALCHEMY_DATABASE_URI="mysql://dlop:dlop@localhost/dlop"
```

3. Run

```bash
# mkdir tmp
# ./run.py
```

task
====
flask/bin/celery -A queue.tasks worker -B -l info

## License
This project is licensed under the [MIT license](http://opensource.org/licenses/MIT).
