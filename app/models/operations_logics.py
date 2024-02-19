from sympy.logic.boolalg import SOPform, simplify_logic
from sympy.abc import A, B, C, D
from sympy.parsing.sympy_parser import parse_expr

def evaluate_expression(expression, values):
    return expression.subs({A: values[0], B: values[1], C: values[2], D: values[3]})


def calculadora_operaciones_logicas(expression_input, A_val, B_val, C_val, D_val):
    
    expression = parse_expr(expression_input)
    # Evaluar la expresión para los valores ingresados
    result = evaluate_expression(expression, [A_val, B_val, C_val, D_val])

    print(result)
    # Simplificar la expresión booleana
    simplified_expression = simplify_logic(expression)

    # Retornae el resultado
    return {
        'valor':f'{"True" if result else "False"}',
        'simplificada': f'{simplified_expression}'
    }

