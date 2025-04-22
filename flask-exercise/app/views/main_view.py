from flask import Blueprint, render_template, current_app
from app.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    # Use current_app.logger to access the configured logger
    current_app.logger.info('Main index route (/) accessed.') # INFO 레벨 로그

    try:
        # Fetch active questions, ordered by creation date descending
        questions = Question.query.filter_by(active=True).order_by(Question.create_date.desc())

        # You can add more detailed logs if needed, e.g., for debugging
        # current_app.logger.debug(f'Querying active questions. Found: {questions.count()}') # DEBUG 레벨 로그 (count()는 쿼리를 실행시킴)
        current_app.logger.debug('Fetched active questions query.') # 쿼리 객체 자체를 로깅
        if questions is None:
            current_app.logger.debug('Questions is None.')
        elif questions.count() == 0:
            current_app.logger.debug('No active questions found.')

        # Render the template with the list of questions
        return render_template('question/question_list.html', question_list=questions)

    except Exception as e:
        # Log any unexpected errors that occur during the process
        current_app.logger.error(f'Error occurred in main index route: {e}', exc_info=True) # ERROR 레벨 로그, exc_info=True는 스택 트레이스를 포함
        # Depending on your error handling strategy, you might want to:
        # 1. Re-raise the exception:
        #    raise
        # 2. Render an error page:
        #    return render_template('error.html', error_message="Sorry, an error occurred."), 500
        # 3. Abort with an error code:
        from flask import abort
        abort(500) # Internal Server Error

# @bp.route('/')
# def index():
#     return render_template('index.html', title='나의 홈페이지', username='게스트')

# @bp.route('/<name>')
# def admin(name: str):
#     return render_template('index.html', title='나의 홈페이지', username=name)

# @bp.route('/hello/<name>/<int:n>')
# def hello(name: str, n: int):
#     return render_template('hello.html', username=name, repeat=n)
