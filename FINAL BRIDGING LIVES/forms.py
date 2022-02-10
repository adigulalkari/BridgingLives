from cProfile import label
from flask import Flask
from flask_wtf import FlaskForm 
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,EqualTo,Email,DataRequired

class RegisterForm(FlaskForm):
    volunteername=StringField(label='Volunteer,your name ?',validators=[Length(min=2,max=20),DataRequired()])
    email=StringField(label='Your Email',validators=[Email(),DataRequired()])
    location=StringField(label='Your location?')
    password1=PasswordField(label='Enter your password ',validators=[Length(min=6),DataRequired()])
    password2=PasswordField(label='Enter your password again',validators=[EqualTo('password1'),DataRequired()])
    submit=SubmitField(label='Create account')
class LoginForm(FlaskForm):
    email=StringField(label='Volunteer, your Email Address',validators=[DataRequired()])
    password=PasswordField(label='Your Password',validators=[DataRequired()])
    submit=SubmitField(label='Log in !')
