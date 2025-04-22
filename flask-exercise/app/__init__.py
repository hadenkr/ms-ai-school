import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
import config

from flask import Flask
from app.database import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    
    db.init_app(app)
    migrate.init_app(app, db)

    from app import models
    from .views import main_view, auth_view, board_view, sql_view

    app.register_blueprint(main_view.bp)
    app.register_blueprint(auth_view.bp)
    app.register_blueprint(board_view.bp)
    app.register_blueprint(sql_view.bp)

    LOG_DIR = 'logs'
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    
    file_handler = RotatingFileHandler(os.path.join(LOG_DIR, 'app.log'), maxBytes=10240, backupCount=10, encoding='utf-8')

    log_level = logging.DEBUG if app.debug else logging.INFO

    file_handler.setLevel(log_level)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    app.logger.addHandler(file_handler)
    app.logger.setLevel(log_level)
    app.logger.info('flask app started')

    return app

# @app.route('/')
# @app.route('/home/')
# @app.route('/index/')
# def index():
#     return 'Hello'

# @app.route('/about/')
# def about():
#     return '회사소개'

# @app.route('/contact/')
# def contact():
#     return '여기로 연락하세요'

# @app.route('/login/<user>')
# def login(user):
#     return f'{user} 님 안녕하세요.'

# @app.route('/logout/')
# def logout():
#     return '아이디와 비번으로 로그아웃'

# @app.route('/board/')
# def board():
#     return '게시판'

# @app.route('/board/<int:id>')
# def board_view(id):
#     print(type(id))
#     return f'게시판 {id} 글 내용'
