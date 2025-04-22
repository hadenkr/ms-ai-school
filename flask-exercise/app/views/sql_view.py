from flask import Blueprint, abort
from app.database import db
from app.models import Answer, Question, User
from datetime import datetime

bp = Blueprint('sql', __name__, url_prefix='/sql')

@bp.route('/create_user/')
def create_user():
    user = User(username='testuser', password='1111', email="test@example.com")
    db.session.add(user)
    db.session.commit()
    return '사용자를 생성했습니다.'

@bp.route('/create/')
def create():
    user = User.query.filter_by(username='testuser').first()
    if user is None:
        abort(404, description='사용자를 찾을 수 없습니다.')
    
    question = Question(
        subject='첫번째 질문',
        content='첫번째 질문입니다.',
        # create_date=datetime.now(),
        ref_user=user)
    db.session.add(question)
    db.session.commit()
    return '질문을 등록했습니다.'

@bp.route('/read/')
def read():
    questions = Question.query.filter_by(active=True).all()
    if questions is None:
        abort(404, description='질문을 찾을 수 없습니다.')
    
    result = ''
    for question in questions:
        result += '{}: {}<br />'.format(question.question_id, question.subject)
    
    return result

@bp.route('/read/<int:id>')
def read_question(id):
    # question = Question.query.get(id)
    question = Question.query.filter_by(question_id=id, active=True).first()
    if question is None:
        abort(404, description='질문을 찾을 수 없습니다.')
    
    result = '{}: {}<br />{}'.format(question.question_id, question.subject, question.content)
    return result

@bp.route('/update/')
def update():
    question = Question.query.get({'question_id': 1, 'active': True})
    if question is None:
        abort(404, description='해당 질문을 찾을 수 없습니다.')
    
    question.subject = '수정된 질문입니다.'
    # question.update_date = datetime.now()
    db.session.commit()
    return '질문이 수정되었습니다.'

@bp.route('/delete/')
def delete():
    question = Question.query.get(1)
    if question is None:
        abort(404, description='해당 질문을 찾을 수 없습니다.')
    
    question.active = False
    # db.session.delete()
    db.session.commit()
    return '질문이 삭제되었습니다.'

@bp.route('/create_answer/')
def create_answer():
    user = User.query.filter_by(username='testuser').first()
    question = Question.query.first()
    if user is None or question is None:
        abort(404, description='사용자 또는 질문을 찾을 수 없습니다.')
    
    answer = Answer(
        content='첫번째 답변입니다.',
        # create_date=datetime.now(),
        ref_question=question,
        ref_user=user
    )
    db.session.add(answer)
    db.session.commit()
    return '답변을 등록했습니다.'
