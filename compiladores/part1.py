"""
1) S    ->      AB
2) B    ->      +AB
3) B    ->      -AB
4) B    ->      E
5) A    ->      CD
6) D    ->      *CD
7) D    ->      /CD
8) D    ->      E
9) C    ->      F
10) F   ->      (S)
11) F   ->      i

reglas_de_produccion = {
    "S": ["AB"],
    "B": ["+AB", "-AB", "E"],
    "A": ["CD"],
    "C": ["F"],
    "D": ["*CD", "/CD", "E"],
    "F": ["(S)", "i"]
}
a+b+c
"""
import re


# Función para extraer caracteres especiales manteniendo el orden
def extraer_caracteres_especiales(cadena):
    caracteres_especiales = []
    
    # Definimos un patrón para caracteres especiales
    patron = re.compile(r'[^a-zA-Z0-9\s]')  # Excluimos letras, números y espacios
    
    # Iteramos sobre cada carácter en la cadena
    for char in cadena:
        if patron.match(char):
            caracteres_especiales.append(char)
    
    return caracteres_especiales


def recorrer_vector(vector):
    # Recorremos el vector y mostramos cada elemento
    numC=0
    for caracter in vector:
        numC+=1
    return numC



def obtener_cadena():
    while True:
        cadena = input("Por favor, ingresa una cadena de texto: ")
        
        if cadena.strip() == "":  # Verifica si la cadena está vacía o solo contiene espacios
            print("Error: No se ha ingresado ningún valor. Intenta de nuevo.")
        else:
            print("Cadena ingresada con éxito:", cadena)
            
            return cadena


cadena_actual= ["s"]
# Llamar a la función para obtener la cadena
cadena = obtener_cadena()

# Eliminar espacios en blanco de la cadena
cadena_final = cadena.replace(" ", "")  # Elimina todos los espacios

# Convertimos la cadena sin espacios en una lista de caracteres
lista_caracteres = list(cadena_final)
print("Cadena ingresada con éxito:", cadena_final)
# Llamamos a la función para recorrer el vector
numC=recorrer_vector(lista_caracteres)

# Imprimir la lista de caracteres
print("Lista de caracteres sin espacios:", lista_caracteres)

print (numC)
  # Extraer caracteres especiales
caracteres_especiales = extraer_caracteres_especiales(cadena_final)
    
print("Caracteres especiales:", caracteres_especiales)
"""for i in range(numC):
    while cadena_final[i]==cadena_actual:
        if cadena_final[i]=="""