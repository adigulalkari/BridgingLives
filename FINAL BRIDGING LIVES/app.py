from django.shortcuts import render
from flask import Flask,flash,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterForm,LoginForm
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_login import login_user
from flask_login import UserMixin
app=Flask(__name__,template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
app.config['SECRET_KEY']='1f6f56a6de60065f6cc5ddd8'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
class Volunteer(db.Model,UserMixin):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(length=20),nullable=False)
    email=db.Column(db.String(length=50),nullable=False,unique=True)
    location=db.Column(db.String(length=30),nullable=False)
    passwordhash=db.Column(db.String(length=60),nullable=False)
    @property
    def password(self):
        return self.password
    @password.setter
    def password(self,plain_text_password):
        self.passwordhash=bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    def check_password_correction(self,attempted_password):
        return bcrypt.check_password_hash(self.passwordhash,attempted_password)


    def __repr__(self):
        return f'Volunteer{self.name}'
    
@login_manager.user_loader
def load_user(user_id):
    return Volunteer.get(user_id)
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('Home.html')
@app.route('/aboutus')
def aboutus_page():
    return render_template('aboutus.html')
@app.route('/contactus')
def contactus_page():
    return render_template('contactus.html')
@app.route('/thanks')
def thanks_page():
    return render_template('thanks.html')
@app.route('/events')
def events_page():
    return render_template('events.html')
@app.route('/vregister',methods=['GET','POST'])
def volunteerregister_page():
    form=RegisterForm()
    if form.validate_on_submit():
        user_to_create = Volunteer(name=form.volunteername.data,email=form.email.data,location=form.location.data,password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('home_page'))
    if form.errors !={}:
        for err_msg in form.errors.values():
            print(f'There was an error in creating your account :{err_msg}')


    return render_template('vregister.html',form=form)
@app.route('/vlogin',methods=['GET','POST'])
def vlogin_page():
    form=LoginForm()
    if form.validate_on_submit():
        attempted_user=Volunteer.query.filter_by(email=form.email.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as :{attempted_user.name} ')
            return render_template(url_for('home_page'))
        else:
            flash('Username and password do not match! Pls try again',category='danger')


    return render_template('vlogin.html',form=form)

