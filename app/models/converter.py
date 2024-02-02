def convertidor(entrada, inicial, final):
    iniciales = {'decimal': 10, 'octal': 8, 'hexadecimal': 16, 'binario': 2}
    finales = {'decimal': 'd', 'octal': 'o', 'hexadecimal': 'X', 'binario': 'b'}

    try:
        arrayDato = entrada.split('.')
        enteros = arrayDato[0]

        decimal = arrayDato[1]
        #convierto las partes enteras a base 10
        entera = int(enteros, iniciales[inicial])
        #luego transformo eso a la base deseada
        result_entera = format(entera, finales[final])

        if(inicial == "decimal" and final == "binario"):
            result_decimal = decimal_a_binario(decimal)
        if(inicial == "decimal" and final == "octal"):
            result_decimal = 0
        if(inicial == "decimal" and final == "hexadecimal"):
            result_decimal = 0
        
        result = str(result_entera) + "." + str(result_decimal)
        return result
    except ValueError:
        return "Invalid input"


def decimal_a_binario(numero):
    decimal_fraccionario = "0."+str(numero)
    decimal_fraccionario=float(decimal_fraccionario)

    parte_decimal = ""
    
    while decimal_fraccionario != 0:
        decimal_fraccionario *= 2
        parte_decimal += str(int(decimal_fraccionario))
        decimal_fraccionario -= int(decimal_fraccionario)
    
    return parte_decimal
