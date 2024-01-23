from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from app import app
#app = Flask(__name__)
#app.config['SECRET_KEY'] = 'your secret key'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/conversor')
def conversor():
    return render_template('conversor.html', dato = 5)

@app.route('/tablas')
def tablas():
    return render_template('tablas.html')
