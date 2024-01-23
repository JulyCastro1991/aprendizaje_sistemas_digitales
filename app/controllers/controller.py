from app.models.converter import convertidor
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/conversor', methods=['GET', 'POST'])
def conversor():
    salida = ''
    entrada = ''
    if request.method == 'POST':
        entrada = request.form['entrada']
        inicial = request.form['inicial']
        final = request.form['final']

        salida = convertidor(entrada, inicial, final)

    return render_template('conversor.html', result = {'entrada': entrada, 'salida': salida})

@app.route('/tablas')
def tablas():
    return render_template('tablas.html')
