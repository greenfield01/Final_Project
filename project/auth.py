from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import User, Ailment
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
    
    login_user(user, remember=remember)
    #return redirect(url_for('main.dashboard'))
    if password == "administratorpass":
        admin = "administrator"
        ailments = Ailment.query.all()
        user = login_user(user, remember=remember)
        return render_template('dashboard.html', admin=admin, user=user, ailments=ailments)
    return redirect(url_for('main.dashboard'))

@auth.route('/forgotpassword')
def forgotpassword():
    return render_template('forgotpassword.html')


@auth.route('/changepassword')
def changepassword():
    return render_template('changepassword.html')



@auth.route('/register')
def register():
    return render_template('register.html')


@auth.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user:
        flash('This email address is already registered!')
        return redirect(url_for('auth.register'))

    new_user = User(email=email, firstname=firstname, lastname=lastname, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
