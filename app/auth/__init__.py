from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy.orm import load_only
from werkzeug.security import generate_password_hash
from app.auth.forms import login_form, register_form
from app.db import db
from app.db.models import User

auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = login_form()
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        else:
            user.authenticated = True
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash("Welcome")
            return redirect(url_for('auth.dashboard'))
    return render_template('login.html', form=form)


@auth.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))
    form = register_form()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            user = User(email=form.email.data, password=generate_password_hash(form.password.data))
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('auth.login'))
        else:
            flash('Already Registered')
            return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)


@auth.route('/dashboard', methods=['POST', 'GET'])
@login_required
def dashboard():
    return render_template('dashboard.html')


@auth.route("/logout")
@login_required
def logout():
    """Logout the current user."""
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/users/<int:user_id>')
@login_required
def retrieve_user(user_id):
    pass


@auth.route('/users/<int:user_id>/edit')
@login_required
def edit_user(user_id):
    pass


@auth.route('/users/<int:user_id>/delete', methods=['POST'])
@login_required
def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User Deleted')
    return redirect('/users', 302)


@auth.route('/users/new')
@login_required
def add_user():
    pass


@auth.route('/users')
@login_required
def browse_users():
    data = User.query.all()
    titles = [('email', 'Email'), ('registered_on', 'Registered On')]
    retrieve_url = ('auth.retrieve_user', [('user_id', ':id')])
    edit_url = ('auth.edit_user', [('user_id', ':id')])
    add_url = url_for('auth.add_user')
    delete_url = ('auth.delete_user', [('user_id', ':id')])
    return render_template('browse.html', titles=titles, add_url=add_url, edit_url=edit_url, delete_url=delete_url,
                           retrieve_url=retrieve_url, data=data, User=User, record_type="Users")
