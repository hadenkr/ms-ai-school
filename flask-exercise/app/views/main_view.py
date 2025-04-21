from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('index.html', title='나의 홈페이지', username='게스트')

@bp.route('/<name>')
def admin(name: str):
    return render_template('index.html', title='나의 홈페이지', username=name)

@bp.route('/hello/<name>/<int:n>')
def hello(name: str, n: int):
    return render_template('hello.html', username=name, repeat=n)
