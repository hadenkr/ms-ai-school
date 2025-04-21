from flask import Flask
from .views import main_view, auth_view, board_view

app = Flask(__name__)
app.register_blueprint(main_view.bp)
app.register_blueprint(auth_view.bp)
app.register_blueprint(board_view.bp)

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
