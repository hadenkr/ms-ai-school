from flask import Blueprint

bp = Blueprint('board', __name__, url_prefix='/question')

@bp.route('/board/')
def board():
    return '게시판'

@bp.route('/board/<int:id>')
def board_view(id):
    return f'게시판 {id} 글 내용'
