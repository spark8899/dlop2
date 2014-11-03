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

2. install and setting MongoDB

```bash
souce install
# groupadd mongodb
# useradd mongodb -g mongodb
# curl -O http://downloads.mongodb.org/linux/mongodb-linux-x86_64-2.6.5.tgz
# tar -zxvf mongodb-linux-x86_64-2.6.4.tgz
# cp -R -n mongodb-linux-x86_64-2.6.4/ /usr/local/mongodb
# chown mongodb:mongodb /usr/local/mongodb -R
# mkdir -p /var/mongodb/data /var/mongodb/logs
# $EDITOR /etc/rc.local
/usr/local/mongodb/bin/mongod --dbpath=/var/mongodb/data --logpath /var/mongodb/logs/log.log -fork

mongodb start
# /usr/local/mongodb/bin/mongod --dbpath=/var/mongodb/data --logpath /var/mongodb/logs/log.log -fork

RPM install
# $EDITOR /etc/yum.repos.d/mongodb.repo
[mongodb]
name=MongoDB Repository
baseurl=http://downloads-distro.mongodb.org/repo/redhat/os/x86_64/
gpgcheck=0
enabled=1

# yum install mongodb-org mongodb-org-server -y
# service mongod start
# chkconfig mongod on

change config.py
===============dlop/config.py===============
MONGODB_DATABASE = "dlop"
MONGODB_HOST = "your's mongodb"
MONGODB_PORT = 27017
MONGODB_USERNAME = None
MONGODB_PASSWORD = None
=============================================================

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
