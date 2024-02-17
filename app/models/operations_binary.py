from app.models.converter import convertidor

def calculadora_binaria(term1, term2, operador):
    try:
        if (operador == '+'):
            result = calcular_operacion(term1, term2, operador)

        if (operador == '-'):
            result = calcular_operacion(term1, term2, operador)

        if (operador == '*'):
            result = calcular_operacion(term1, term2, operador)

        if (operador == '/'):
            result = calcular_operacion(term1, term2, operador)
        
        return result
    except ValueError:
        return "Invalid input"

def calcular_operacion(term1, term2, operador):
    term1 = convertidor(term1, 'binario', 'decimal')
    term2 = convertidor(term2, 'binario', 'decimal')
    #opero
    operacion = eval(term1 + operador + term2)
    suma_str = str(operacion)
    #convierto en binario
    result = convertidor(suma_str, 'decimal', 'binario')

    return result
