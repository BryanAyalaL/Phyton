# Tokens de entrada (por ejemplo, ID, *, -, /, etc.)
tokens = []  # Lista de tokens de entrada
current_token = None  # Token actual
pos = -1  # Posición del token actual

def next_token():
    """Avanza al siguiente token"""
    global current_token, pos
    pos += 1
    if pos < len(tokens):
        current_token = tokens[pos]
    else:
        current_token = None

def match(expected_token):
    """Verifica si el token actual coincide con el esperado"""
    global current_token
    if current_token == expected_token:
        next_token()
    else:
        raise SyntaxError(f"Error de sintaxis: se esperaba '{expected_token}' pero se encontró '{current_token}'")

def S():
    """Regla S => AB"""
    print("S -> AB")
    A()
    B()

def A():
    """Regla A => CD"""
    print("A -> CD")
    C()
    D()

def B():
    """Regla B => AB | -AB | ε"""
    if current_token == 'ID':
        print("B -> +AB")
        A()
        B()
    elif current_token == '-':
        print("B -> -AB")
        match('-')
        A()
        B()
    else:
        # Producción vacía (ε)
        print("B -> epsilon")  # Cambiado a "epsilon"

def C():
    """Regla C => F"""
    print("C -> F")
    F()

def D():
    """Regla D => *CD | /CD | ε"""
    while current_token in ('*', '/'):
        if current_token == '*':
            print("D -> *CD")
            match('*')
        elif current_token == '/':
            print("D -> /CD")
            match('/')
        C()  # Llama a C después de * o /
    print("D -> epsilon")  # Cambiado a "epsilon"

def F():
    """Regla F => ID"""
    if current_token == 'ID':
        print("F -> ID")
        match('ID')
    else:
        raise SyntaxError(f"Error de sintaxis: se esperaba 'ID' pero se encontró '{current_token}'")

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
input_tokens = ['ID', '-', 'ID', 'ID', 'ID', '+', 'ID', '/', 'ID']  # Ejemplo de tokens de entrada
try:
    parse(input_tokens)
except SyntaxError as e:
    print(e)
