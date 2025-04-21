from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup/')
def signup():
    return '회원가입'

@bp.route('/login/')
def login():
    return '아이디와 비번으로 로그인'

@bp.route('/logout/')
def logout():
    return '로그아웃'
