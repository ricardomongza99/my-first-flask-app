from app import app
from flask import render_template, request, redirect, url_for
from utils import valid_username, valid_password

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/', methods=['POST'])
def login_form():
    username = request.form['username']
    password = request.form['password']

    if valid_username(username) and valid_password(password):
        return redirect(url_for('home'))
    
    return render_template('login.html')

@app.route('/home')
def home():
    return "Welcome back!"