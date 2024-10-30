# Ejemplo de abs()

numero_positivo = 10
numero_negativo = -20

print(abs(numero_positivo))  # Retorna 10, ya que es el valor absoluto
print(abs(numero_negativo))  # Retorna 20, el valor absoluto de -20

print("========================================")

# Ejemplo de all()

# Todos los elementos son verdaderos
lista_verdadera = [True, 1, "Texto", [1, 2]]
print(all(lista_verdadera))  # Retorna True

# Un elemento es falso
lista_falsa = [True, 0, "Texto"]
print(all(lista_falsa))  # Retorna False, ya que 0 es considerado falso

# Lista vacía
lista_vacia = []
print(all(lista_vacia))  # Retorna True, ya que una lista vacía se considera verdadera en este caso

print("========================================")

# Ejemplo de any()

# Un elemento es verdadero
verdadero_un_elemento= [True, 0, "", []]
print(any(verdadero_un_elemento)) #Retorna verdadero por que un elemento es verdadero

# Lista Falsa
lista_falsa=[ 0, "", []]
print(any(lista_falsa)) # Retorna falso por que no hay valores verdaderos

#lista vacia
lista_vacia=[]
print(any(lista_vacia)) # Retorna False, ya que una lista vacía se considera falsa en este caso

print("========================================")

#ASCII se usa pra pasar una cadena de texto a su 127 letras o numero su forma inglesa, siempre empiezan con / invertido
# Texto con caracteres no ASCII
texto = 'Héllo, Привет, 你好'

# Uso de ascii()
resultado = ascii(texto)

# Imprimir el texto
print(texto)
# Imprimir el resultado
print(resultado)

print("========================================")

# Funcion bin, convierte el numero a su forma decimal
print(bin(3))  # 3 en decimal es 11 en binario
print(bin(-10))  # -10 en decimal es -1010 en binario

print("========================================")

#Clase bool, cualquiero valor que sea vacido, nulo sera false
print(bool())  # Sin argumento
print(bool(0))      # El número 0 es falso
print(bool(""))     # La cadena vacía es falsa
print(bool([]))     # La lista vacía es falsa
print(bool(None))   # None es falso

print(bool(1))      # El número 1 es verdadero
print(bool("Hola")) # Las cadenas no vacías son verdaderas
print(bool([1, 2])) # Las listas no vacías son verdaderas

print("========================================")

#breakpoint es una funcion para detener el programa y poder moverse desde ese punto
def ejemplo():
    x = 10
    y = 20
    ## breakpoint()  # Se detendrá aquí para iniciar el depurador y se manneja con {n(n (next)),c(c (continue)),q(q (quit),p(p variable)}
    z = x + y
    print(z)

ejemplo()

print("========================================")

#bytearray es una secuencia mutable de bytes, adecuada para situaciones donde necesitas modificar el contenido.
ba = bytearray("Hola", "utf-8")
print(ba)
ba = bytearray(5)  # Crea un bytearray de 5 bytes, todos inicializados en 0
print(ba)
ba = bytearray(b'Hola Mundo')  # Inicializando desde un objeto bytes
print(ba)
ba = bytearray([72, 101, 108, 108, 111])  # Inicializando con una lista de enteros
print(ba)
ba = bytearray()  # Inicializando sin argumentos
print(ba)
ba = bytearray(b"Hola")
ba[0] = 104  # Cambiando el primer byte
print(ba)
ba = bytearray(b"Hola")
ba.append(33)  # Agrega el byte del signo de exclamación
print(ba)

print("========================================")

#bytes es una secuencia inmutable de bytes, ideal para datos que no necesitan ser modificados.
b = bytes("Hola", "utf-8")
print(b)

b = bytes(5)  # Crea un objeto bytes de 5 bytes, todos inicializados en 0
print(b)

b = bytes(bytearray(b'Hola Mundo'))  # Inicializando desde un bytearray
print(b)

b = bytes([72, 101, 108, 108, 111])  # Inicializando con una lista de enteros
print(b)


print("========================================")

#callable se utiliza para determinar si un objeto se puede invocar o llamar como una función. Es útil para verificar si un objeto tiene la capacidad de ser llamado, lo que significa que puede ser ejecutado como una función o un método.
# Ejemplo 1: Funciones
def my_function():
    return "Hola"

print(callable(my_function))  # Salida: True

# Ejemplo 2: Clases
class MyClass:
    pass

print(callable(MyClass))  # Salida: True

# Creando una instancia de MyClass
instance = MyClass()
print(callable(instance))  # Salida: False, porque no se ha definido __call__

# Ejemplo 3: Clases con __call__
class CallableClass:
    def __call__(self):
        return "Soy invocable"

callable_instance = CallableClass()
print(callable(callable_instance))  # Salida: True, porque tiene un método __call__

# Ejemplo 4: Tipos de datos no invocables
number = 42
print(callable(number))  # Salida: False

text = "Hola"
print(callable(text))  # Salida: False

print("========================================")

#chr  se utiliza para convertir un número entero que representa un punto de código Unicode en su correspondiente carácter de cadena. Esta función es particularmente útil cuando se trabaja con codificaciones y representaciones de caracteres, ya que permite obtener el carácter asociado a un valor específico en el estándar Unicode.
# Ejemplo 1: Carácter 'a'
code_point_a = 97
char_a = chr(code_point_a)
print(char_a)  # Salida: 'a'

# Ejemplo 2: Carácter '€'
code_point_euro = 8364
char_euro = chr(code_point_euro)
print(char_euro)  # Salida: '€'

# Ejemplo 3: Carácter de un emoji
code_point_smiling_face = 128512  # Código Unicode para 😀
char_smiling_face = chr(code_point_smiling_face)
print(char_smiling_face)  # Salida: '😀'

# Ejemplo 4: Valor fuera de rango
try:
    char_invalid = chr(1114112)  # Fuera del rango válido
except ValueError as e:
    print(e)  # Salida: chr() arg not in range(0x110000)

print("========================================")
#classmethod Un método de clase es un tipo especial de método en la programación orientada a objetos que pertenece a la clase en sí misma, no a las instancias de esa clase. A diferencia de un método de instancia, que actúa sobre un objeto o instancia específica, un método de clase actúa sobre la clase como un todo. Este método recibe la clase como su primer argumento, en lugar de una instancia.
class Persona:
    numero_de_personas = 0  # Atributo de clase

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Persona.numero_de_personas += 1  # Incrementar el número de personas cada vez que se crea una instancia

    @classmethod
    def mostrar_numero_de_personas(cls):  # Método de clase
        print(f"Hay {cls.numero_de_personas} personas.")

# Crear algunas instancias
persona1 = Persona("Alice", 30)
persona2 = Persona("Bob", 25)

# Llamar al método de clase sin crear una instancia
Persona.mostrar_numero_de_personas()  # Salida: Hay 2 personas.
