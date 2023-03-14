from flask import render_template, flash, redirect, url_for, request
from . import auth
from .forms import LoginForm
from ..models import User, Role
from .forms import RoleForm, UserForm
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db

@auth.route('/' , methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)

@auth.route('/register_user' , methods=['GET', 'POST'])
def register_user():
    users = User.query.order_by(User.id.desc()).all()
    form_user = UserForm()
    if form_user.validate_on_submit():
        user = User.query.filter_by(email=form_user.email.data).first()
        if user is None:
            # Hash the password
            hashed_pw = generate_password_hash(form_user.password.data, 'sha256')
            user = User(username=form_user.username.data, email=form_user.email.data,
                        password_hash=hashed_pw, role_id=form_user.role.data)
            db.session.add(user)
            db.session.commit()
            form_user.username.data = ''
            form_user.email.data = ''
            form_user.password.data = ''
            flash(f'User {user.email} added')
        return redirect(url_for('auth.register_user'))
    else:
        flash('Error: User already exists')
    #role = Role(name='Admin')
    return render_template('auth/register_user.html', form_user=form_user, users=users)

@auth.route('/register_role' , methods=['GET', 'POST'])
def register_role():
    roles = Role.query.order_by(Role.id.desc()).all()
    form_role = RoleForm()

    if form_role.validate_on_submit():
        role = Role(name=form_role.name.data)
        db.session.add(role)
        db.session.commit()

        flash('User Added')
    #role = Role(name='Admin')
    return render_template('auth/register_role.html', form_role=form_role, roles=roles)