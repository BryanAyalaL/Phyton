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
    breakpoint()  # Se detendrá aquí para iniciar el depurador y se manneja con {n(n (next)),c(c (continue)),q(q (quit),p(p variable)}
    z = x + y
    print(z)

ejemplo()

print("========================================")

