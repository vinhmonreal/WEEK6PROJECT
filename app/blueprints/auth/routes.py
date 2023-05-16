from flask import render_template, flash, redirect, url_for
from app.forms import RegistrationForm, LoginForm
from app.models import User
from . import bp
from flask_login import login_user, logout_user, current_user, login_required


@bp.route('/register', methods=['GET', 'POST'])

def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        if not User.query.filter_by(email=form.email.data).first() and not User.query.filter_by(username=form.username.data).first():
            user = User(username=form.username.data, email=form.email.data)
            user.hash_password(form.password.data)
            user.add_token()
            user.commit()
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('auth.login'))
        elif User.query.filter_by(email=form.email.data).first():
            flash(f'Email already exists', 'danger')
        else:
            flash(f'Username already exists', 'danger')
    return render_template('register.jinja', title='Register', form=form)

#fixig this for incperection password
@bp.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            flash(f'{form.username.data} signed in','success')
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            flash(f'{form.username.data} doesn\'t exist or incorrect password','warning')
    return render_template('login.jinja', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))