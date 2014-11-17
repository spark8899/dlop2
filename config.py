import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = '3xLntKKFRZITY423'

MYSQL_DATABASE_USER="dlop"
MYSQL_DATABASE_PASSWORD="dlop"
MYSQL_DATABASE_DB="dlop"
MYSQL_DATABASE_HOST="localhost"

SQLALCHEMY_DATABASE_URI="mysql://dlop:dlop@localhost/dlop"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_BINDS = {
    'dlop': 'mysql://dlop:dlop@localhost/dlog',
}
TABLE_PREFIX = "dlop_"
