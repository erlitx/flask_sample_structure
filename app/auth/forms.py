from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, equal_to


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class RoleForm(FlaskForm):
    name = StringField('Role Name', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('Register')



class UserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired(), equal_to('password_repeat', message='Passwords Must Match!')])
    password_repeat = PasswordField('Repeat Password', validators=[DataRequired()])
    role = SelectField('Role', choices=[('1', 'Admin'), ('3', 'User')])
    submit = SubmitField('Register')
