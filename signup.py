from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email

class SignupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    nid = StringField('National ID', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class SearchForm(FlaskForm):
    nid = StringField('National ID', validators=[DataRequired()])
    submit = SubmitField('Search')

