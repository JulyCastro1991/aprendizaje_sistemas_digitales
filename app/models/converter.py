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


        #Binario a:
        if(inicial == "binario" and final == "decimal"):
            result_decimal = cualquier_base_a_decimal(decimal,2)

        if(inicial == "binario" and final == "octal"):
            result_decimal = binario_a_octal(decimal)

        if(inicial == "binario" and final == "hexadecimal"):
            result_decimal = binario_a_hexadecimal(decimal)


        #Decimal a:
        if(inicial == "decimal" and final == "binario"):
            result_decimal = decimal_a_binario(decimal)
        
        if(inicial == "decimal" and final == "octal"):
            result_decimal = decimal_a_octal(decimal)
            
        if(inicial == "decimal" and final == "hexadecimal"):
            result_decimal = decimal_a_hexadecimal(decimal)


        #Octal a:
        if(inicial == "octal" and final == "binario"):
            result_decimal = octal_a_binario(decimal)
        
        if(inicial == "octal" and final == "decimal"):
            result_decimal = cualquier_base_a_decimal(decimal,8)
        
        if(inicial == "octal" and final == "hexadecimal"):
            binario = octal_a_binario(decimal)
            result_decimal = binario_a_hexadecimal(binario)


        #Hexadecimal a:
        if(inicial == "hexadecimal" and final == "binario"):
            result_decimal = hexadecimal_a_binario(decimal)            

        if(inicial == "hexadecimal" and final == "decimal"):
            result_decimal = cualquier_base_a_decimal(decimal,16)

        if(inicial == "hexadecimal" and final == "octal"):
            binario = hexadecimal_a_binario(decimal)
            result_decimal = binario_a_octal(binario)
        
        
        result = str(result_entera) + "." + str(result_decimal)
        return result
    except ValueError as e:
        print(e)
        return "Invalid input"




#Solo transforman la parte decimal

def binario_a_octal(numero):

    # Agrega ceros a la derecha si es necesario para completar los grupos de tres dígitos
    while len(numero) % 3 != 0:
        numero = numero +'0'

    # Divide el número binario en grupos de tres
    grupos_binarios = [numero[i:i+3] for i in range(0, len(numero), 3)]

    numero_octal = ''.join(str(int(grupo_binario, 2)) for grupo_binario in grupos_binarios)

    return numero_octal

def binario_a_hexadecimal(numero):

    # Agrega ceros a la derecha si es necesario para completar los grupos de tres dígitos
    while len(numero) % 4 != 0:
        numero = numero +'0'

    # Divide el número binario en grupos de tres
    grupos_binarios = [numero[i:i+4] for i in range(0, len(numero), 4)]

    numero_hexadecimal = ''.join(str(hex(int(grupo_binario, 2))[2:]) for grupo_binario in grupos_binarios)

    return numero_hexadecimal.upper()


def decimal_a_binario(numero):
    decimal_fraccionario = "0."+str(numero)
    decimal_fraccionario=float(decimal_fraccionario)

    respuesta = ""
    
    aux = 1
    controlador = 1
    #20 BITS
    while (controlador <= 20) and (aux != 0.0):
        decimal_fraccionario *= 2
        temp = str(decimal_fraccionario).split('.')
        respuesta += temp[0]
        decimal_fraccionario = float("0."+temp[1])
        aux = float(temp[1])
        controlador += 1

    return respuesta

def decimal_a_binario2(numero):
    decimal_fraccionario = "0."+str(numero)
    decimal_fraccionario=float(decimal_fraccionario)

    respuesta = ""
    
    while decimal_fraccionario != 0:
        decimal_fraccionario *= 2
        respuesta += str(int(decimal_fraccionario))
        decimal_fraccionario -= int(decimal_fraccionario)

    return respuesta


def decimal_a_octal(numero):
    decimal_fraccionario = "0."+str(numero)
    decimal_fraccionario=float(decimal_fraccionario)

    respuesta = ""
    
    aux = 1
    controlador = 1
    #20 BITS
    while (controlador <= 20) and (aux != 0.0):
        decimal_fraccionario *= 8
        temp = str(decimal_fraccionario).split('.')
        respuesta += temp[0]
        decimal_fraccionario = float("0."+temp[1])
        aux = float(temp[1])
        controlador += 1

    return respuesta

def decimal_a_hexadecimal(numero):
    decimal_fraccionario = "0."+str(numero)
    decimal_fraccionario=float(decimal_fraccionario)

    respuesta = ""
    
    aux = 1
    controlador = 1
    #20 BITS
    while (controlador <= 20) and (aux != 0.0):
        decimal_fraccionario *= 16
        temp = str(decimal_fraccionario).split('.')
        respuesta += str(hex(int(temp[0])))[2:]
        decimal_fraccionario = float("0."+temp[1])
        aux = int(temp[1])
        controlador += 1

    return respuesta.upper()

def octal_a_binario(numero):
    numeros = [*str(numero)]

    numero_binario = ""
    #mandar a agregar 0
    for numero in numeros:
        binario = str(bin(int(numero))[2:])

        while len(binario) % 3 != 0:
            binario = '0'+binario
        
        numero_binario += binario

    return numero_binario


def hexadecimal_a_binario(numero):
    numeros = [*str(numero)]

    numero_binario = ""
    #mandar a agregar 0
    for numero in numeros:
        binario = str(bin(int(numero,16))[2:])

        while len(binario) % 4 != 0:
            binario = '0'+binario
        
        numero_binario += binario

    return numero_binario

def hexadecimal_a_octal(numero):
    numeros = [*str(numero)]

    numero_binario = ""

    return numero_binario


def cualquier_base_a_decimal(numero, base):
    numeros = [*str(numero)]

    parte_decimal = 0

    aux = -1
    for x in numeros:
        x = int(x, base)
        parte_decimal += int(x)*(base**aux)
        aux -= 1

    parte_decimal = str(parte_decimal).split('.')

    return parte_decimal[1]
