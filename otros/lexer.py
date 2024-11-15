import re

# Definir las expresiones regulares para cada tipo de token
token_specification = [
    ('KEYWORD',   r'\b(while|else)\b'),  # Palabras clave: while, else
    ('IDENTIFIER', r'[A-Za-z_][A-Za-z0-9_]*'),  # Identificadores (variables, funciones)
    ('NUMBER',    r'\b\d+\b'),  # Números (enteros)
    ('OPERATOR',  r'[+\-=\*/<>]'),  # Operadores
    ('COLON',     r':'),  # Dos puntos
    ('LPAREN',    r'\('),  # Paréntesis izquierdo
    ('RPAREN',    r'\)'),  # Paréntesis derecho
    ('SKIP',      r'[ \t\n]+'),  # Espacios en blanco y saltos de línea (se ignoran)
    ('MISMATCH',  r'.'),  # Cualquier otro carácter no reconocido
]

# Crear un patrón de expresiones regulares para combinar todas las expresiones anteriores
master_pattern = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)

# Lexer: Función que recibe una cadena de texto y devuelve los tokens
def lexer(code):
    line_number = 1
    line_start = 0
    for mo in re.finditer(master_pattern, code):
        kind = mo.lastgroup  # Tipo de token
        value = mo.group()  # Valor del token
        if kind == 'SKIP':  # Ignorar espacios en blanco y saltos de línea
            continue
        elif kind == 'MISMATCH':  # Si encontramos algo que no es un token válido
            raise RuntimeError(f'Error de lexema inesperado: {value} en la línea {line_number}')
        else:
            # Devolver el token (tipo, valor)
            yield kind, value

# Ejemplo de código fuente a analizar
code = """
while (x < 10):
    xas2=2+x
else:
    y = x * 2
"""

# Usamos el lexer para tokenizar el código
tokens = list(lexer(code))

# Imprimir los tokens generados
for token in tokens:
    print(token)
print(master_pattern)