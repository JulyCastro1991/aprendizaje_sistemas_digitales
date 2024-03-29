from app.models.converter import convertidor
from app.models.operations_binary import calculadora_binaria
from app.models.operations_logics import calculadora_operaciones_logicas
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from app import app
import requests
# import serial

# puerto_serie = serial.Serial('COM3', 115200, timeout=1)

ip_servidor = 'http://192.168.137.219'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/operaciones_binarias', methods=['GET', 'POST'])
def operaciones_binarias():
    if request.method == 'POST':
        term1 = request.form['term1']
        term2 = request.form['term2']
        operador = request.form['operador']
        salida = calculadora_binaria(term1, term2, operador)

        return salida

    return render_template('operaciones_binarias.html')

@app.route('/operaciones_binarias_esp', methods=['POST'])
def operaciones_binarias_esp():
    if request.method == 'POST':
        term1 = request.form['term1']
        term2 = request.form['term2']
        operador = request.form['operador']
        salida = calculadora_binaria(term1, term2, operador)
        resp = requests.post(f'{ip_servidor}/operaciones_binarias', data=salida)

        return salida


@app.route('/conversor', methods=['GET', 'POST'])
def conversor():
    if request.method == 'POST':
        entrada = request.form['entrada']
        inicial = request.form['inicial']
        final = request.form['final']
        salida = convertidor(entrada, inicial, final)
        # puerto_serie.write(str(salida).encode())
        resp = requests.post(f'{ip_servidor}', data=salida)

        return  salida
    
    return render_template('conversor.html')


@app.route('/operaciones_logicas', methods=['GET', 'POST'])
def operaciones_logicas():
    if request.method == 'POST':
        expression = request.form['expression']
        A_val = request.form['A_val']
        B_val = request.form['B_val']
        C_val = request.form['C_val']
        D_val = request.form['B_val']

        salida = calculadora_operaciones_logicas(expression, A_val,  B_val, C_val, D_val)

        return  salida
        
    return render_template('operaciones_logicas.html')

@app.route('/operaciones_logicas_esp', methods=['POST'])
def operaciones_logicas_esp():
    if request.method == 'POST':
        expression = request.form['expression']
        A_val = request.form['A_val']
        B_val = request.form['B_val']
        C_val = request.form['C_val']
        D_val = request.form['B_val']

        salida = calculadora_operaciones_logicas(expression, A_val,  B_val, C_val, D_val)
        data = (str(salida['valor']) + "\n" + "Funcion: "+ "\n" + str(salida['simplificada'])).encode() 
        requests.post(f'{ip_servidor}/operaciones_logicas', data=data)

        return  salida

@app.route('/mostrar_tabla', methods=['POST'])
def mostrar_tabla():
    if request.method == 'POST':
        data = request.args.get("contador", "")
        
        print(data)
        requests.post(f'{ip_servidor}/mostrar_tabla', data=data)

        return  "OK"