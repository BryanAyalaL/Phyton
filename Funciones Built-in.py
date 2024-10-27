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

