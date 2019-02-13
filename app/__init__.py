from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

app = Flask(__name__)
app.config.from_object(Config)

from app.auth import bp as auth_bp
app.register_blueprint(auth_bp,url_prefix='/auth')

from app.main import bp as main_bp
app.register_blueprint(main_bp)

from app import models
