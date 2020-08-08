import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'not-guessable')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BLOGGING_URL_PREFIX = '/blog'
    BLOGGING_DISQUS_SITENAME = 'test'
    BLOGGING_SITEURL = 'http://localhost:5000'
    BLOGGING_SITENAME = 'TeachUs'
    BLOGGING_KEYWORDS = ['blog', 'meta', 'keywords']
    FILEUPLOAD_LOCALSTORAGE_IMG_FOLDER = 'img_upload'
    FILEUPLOAD_PREFIX = '/fileupload'
    FILEUPLOAD_ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']
