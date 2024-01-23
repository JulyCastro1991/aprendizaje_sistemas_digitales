def convertidor(entrada, inicial, final):
    iniciales = {'decimal': 10, 'octal': 8, 'hexadecimal': 16, 'binario': 2}
    finales = {'decimal': 'd', 'octal': 'o', 'hexadecimal': 'X', 'binario': 'b'}

    try:
        decimal_value = int(entrada, iniciales[inicial])
        result = format(decimal_value, finales[final])
        return result
    except ValueError:
        return "Invalid input"