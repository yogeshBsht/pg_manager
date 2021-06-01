from flask import render_template
from app.auth import bp
from app.auth.forms import LoginForm

@bp.route('/')
@bp.route('/index')
def index():
    return "Hello. This is PG Manager."
    
@bp.route('/login')
def login():
    form = LoginForm()
    return render_template('auth/login.html', title='Sign In', form=form)
