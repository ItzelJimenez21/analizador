import ply.yacc as yacc
from lex import tokens  # Importa los tokens desde lexico2.py

# Reglas de la gramática
def p_for_loop_correct(p):
    '''statement : PR'''
    print("Estructura correcta: bucle for")
    p[0] = ('for_loop', p[1], 'correcta')

def p_for_loop_incorrect(p):
    '''statement : ID'''
    if p[1] in ["Hola", "Mundo", "Hola mundo"]:
        print(f"Estructura incorrecta, identificador especial: {p[1]}")
        p[0] = ('special_identifier', p[1], 'incorrecta')
    else:
        print("Estructura incorrecta")
        p[0] = ('identifier', p[1], 'incorrecta')

# Manejo de errores sintácticos
def p_error(p):
    print("Error de sintaxis en '%s'" % p.value)

# Construir el analizador sintáctico
parser = yacc.yacc()

def sintactico(text):
    result = parser.parse(text)
    return result