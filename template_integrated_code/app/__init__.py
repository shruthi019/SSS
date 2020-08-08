from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_blogging import SQLAStorage, BloggingEngine

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
engine = create_engine('sqlite:////tmp/blog.db')
meta = MetaData()
sql_storage = SQLAStorage(engine, metadata=meta)
blog_engine = BloggingEngine(app, sql_storage)
loginmanager = LoginManager(app)
loginmanager.login_view = 'login'
meta.create_all(bind=engine)

from app import models, routes

