def calculadora_binaria(term1, term2, operador):
    try:
        if (operador == '+'):
            result = binary_addition(term1,term2)
        if (operador == '-'):
            result = binary_subtraction(term1,term2)
        if (operador == '*'):
            result = binary_multiplication(term1,term2)
        if (operador == '/'):
            result = binary_division(term1,term2)
        
        return result
    except ValueError:
        return "Invalid input"

def binary_addition(a, b):
    # Dividir los números en partes enteras y fraccionarias
    a_integer, a_fraction = a.split('.')
    b_integer, b_fraction = b.split('.')

    # Alinear las partes fraccionarias agregando ceros
    max_fraction_length = max(len(a_fraction), len(b_fraction))
    a_fraction = a_fraction.ljust(max_fraction_length, '0')
    b_fraction = b_fraction.ljust(max_fraction_length, '0')

    # Sumar las partes fraccionarias
    fraction_sum = bin(int(a_fraction, 2) + int(b_fraction, 2))[2:]

    # Sumar las partes enteras
    integer_sum = bin(int(a_integer, 2) + int(b_integer, 2))[2:]

    # Si la suma de la parte fraccionaria es mayor o igual a 1, ajustar la parte entera
    if len(fraction_sum) > max_fraction_length:
        integer_sum = bin(int(integer_sum, 2) + 1)[2:]
        fraction_sum = fraction_sum[1:]  # Eliminar el primer bit

    # Alinear la parte fraccionaria a la longitud máxima
    fraction_sum = fraction_sum.rjust(max_fraction_length, '0')

    # Combinar la parte entera y la parte fraccionaria con un punto en el medio
    result = f"{integer_sum}.{fraction_sum}"

    return result

def binary_subtraction(a, b):
    # Dividir los números en partes enteras y fraccionarias
    a_integer, a_fraction = a.split('.')
    b_integer, b_fraction = b.split('.')

    # Alinear las partes fraccionarias agregando ceros
    max_fraction_length = max(len(a_fraction), len(b_fraction))
    a_fraction = a_fraction.ljust(max_fraction_length, '0')
    b_fraction = b_fraction.ljust(max_fraction_length, '0')

    # Restar las partes fraccionarias
    fraction_difference = bin(int(a_fraction, 2) - int(b_fraction, 2))[2:]

    # Restar las partes enteras
    integer_difference = bin(int(a_integer, 2) - int(b_integer, 2))[2:]

    # Si la resta de la parte fraccionaria es menor que 0, ajustar la parte entera
    if len(fraction_difference) < max_fraction_length:
        integer_difference = bin(int(integer_difference, 2) - 1)[2:]
        fraction_difference = bin(int(fraction_difference, 2) + 2**max_fraction_length)[2:]

    # Alinear la parte fraccionaria a la longitud máxima
    fraction_difference = fraction_difference.rjust(max_fraction_length, '0')

    # Combinar la parte entera y la parte fraccionaria con un punto en el medio
    result = f"{integer_difference}.{fraction_difference}"

    return result

def binary_multiplication(a, b):
    # Eliminar el punto decimal y convertir los números a enteros
    a = a.replace('.', '')
    b = b.replace('.', '')

    # Convertir los números binarios a enteros
    int_a = int(a, 2)
    int_b = int(b, 2)

    # Multiplicar los enteros
    result = int_a * int_b

    # Convertir el resultado de nuevo a binario
    result_binary = bin(result)[2:]

    # Contar la cantidad de dígitos en la parte fraccionaria
    fraction_digits = len(a.split('.')[-1]) + len(b.split('.')[-1])

    # Insertar el punto decimal en la posición correcta
    integer_part = result_binary[:-fraction_digits]
    fraction_part = result_binary[-fraction_digits:]

    if len(integer_part) == 0:
        integer_part = '0'

    # Insertar el punto decimal
    if len(integer_part) < len(fraction_part):
        integer_part = '0' * (len(fraction_part) - len(integer_part)) + integer_part

    result_binary = f"{integer_part}.{fraction_part}"

    return result_binary

def binary_division(a, b):
    # Eliminar el punto decimal y convertir los números a enteros
    a = a.replace('.', '')
    b = b.replace('.', '')

    # Convertir los números binarios a enteros
    int_a = int(a, 2)
    int_b = int(b, 2)

    # Realizar la división de enteros
    quotient = int_a / int_b

    # Convertir el resultado de nuevo a binario
    quotient_binary = bin(int(quotient))[2:]

    # Restaurar el punto decimal en el resultado
    if len(quotient_binary) < len(a):
        quotient_binary = '0' * (len(a) - len(quotient_binary)) + quotient_binary

    # Insertar el punto decimal en la posición correcta
    integer_part = quotient_binary[:-len(a.split('.')[-1])]
    fraction_part = quotient_binary[-len(a.split('.')[-1]):]

    if len(integer_part) == 0:
        integer_part = '0'

    result_binary = f"{integer_part}.{fraction_part}"

    return result_binary
