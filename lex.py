import ply.lex as lex

# Definir los tokens
tokens = ['PR', 'ID']

# Definir las expresiones regulares para los tokens
t_PR = r'\b[Ff]or\b'  # Palabra reservada (for y For)

# Definir un token para identificadores
def t_ID(t):
    r'\b\w+(\s\w+)*\b'  # Permite palabras simples o compuestas como "Hola mundo"
    if t.value.lower() == 'for':  # Si es "for" o "For", debe ser PR
        t.type = 'PR'
    elif t.value in ["Hola mundo", "Hola", "Mundo"]:  # Excepciones como identificadores
        t.type = 'ID'
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Función para manejar los saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Función para manejar los errores léxicos
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Inicializar el lexer
lexer = lex.lex()

def lexico(text):
    lexer.input(text)
    lexemes = []

    while True:
        tok = lexer.token()
        if not tok:
            break  # No más tokens
        lexeme = (tok.type, tok.value, tok.lineno)
        lexemes.append(lexeme)

    return lexemes