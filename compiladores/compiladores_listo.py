tokens = []  # Lista de tokens de entrada
current_token = None  # Token actual
pos = -1  # Posición del token actual

def next_token():
    """Avanza al siguiente token."""
    global current_token, pos
    pos += 1
    if pos < len(tokens):
        current_token = tokens[pos]
    else:
        current_token = None

def match(expected_token):
    """Verifica si el token actual coincide con el esperado."""
    global current_token
    if current_token == expected_token:
        next_token()
    else:
        raise SyntaxError(f"Error de sintaxis: se esperaba '{expected_token}' pero se encontró '{current_token}'")

def S():
    """Regla S -> AB"""
    print("S -> AB")
    A()
    B()

def A():
    """Regla A -> CD"""
    print("A -> CD")
    C()
    D()

def B():
    """Regla B -> +AB | -AB | E"""
    if current_token == '+':
        print("B -> +AB")
        match('+')
        A()
        B()
    elif current_token == '-':
        print("B -> -AB")
        match('-')
        A()
        B()
    else:
        # Producción vacía (Epsilon)
        print("B -> E")

def C():
    """Regla C -> F"""
    print("C -> F")
    F()

def D():
    """Regla D -> *CD | /CD | E"""
    if current_token == '*':
        print("D -> *CD")
        match('*')
        C()
        D()
    elif current_token == '/':
        print("D -> /CD")
        match('/')
        C()
        D()
    else:
        # Producción vacía (Epsilon)
        print("D -> E")

def F():
    """Regla F -> (S) | i"""
    if current_token == '(':
        print("F -> (S)")
        match('(')
        S()
        match(')')
    elif current_token == 'i':
        print("F -> i")
        match('i')
    else:
        raise SyntaxError(f"Error de sintaxis: se esperaba '(' o 'i', pero se encontró '{current_token}'")

# Función para iniciar el análisis
def parse(input_tokens):
    global tokens, pos
    tokens = input_tokens
    pos = -1
    next_token()  # Iniciar con el primer token
    S()  # Comienza desde el símbolo inicial S
    if current_token is not None:
        raise SyntaxError("Error de sintaxis: la entrada no se consumió completamente")
    else:
        print("Análisis completado exitosamente.")

# Ejemplo de uso
input_tokens = ['i', '+', 'i', '*', 'i', '-', '(', 'i', '+', 'i', ')']
try:
    parse(input_tokens)
except SyntaxError as e:
    print(e)
