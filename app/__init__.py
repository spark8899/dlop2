from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
#from config import *

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models

#def register_blueprints(app):
#    # Prevents circular imports
#    from app.assets_manage import assets
#    from app.project_manage import project
#    from app.script_manage import myscript
#    app.register_blueprint(assets)
#    app.register_blueprint(project)
#    app.register_blueprint(myscript)

#register_blueprints(app)

#logger file setting
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/dlop.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('dlop logging startup')
