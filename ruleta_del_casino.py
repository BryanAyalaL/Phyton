import random

colores=["rojo","negro"]
numeros=range(0,37)

numero_usuario=int(input("Elige un numero: "))
color_usuario=input("Elige un color: ")

if numero_usuario not in numeros or color_usuario.lower() not in colores:
    print("Error, datos no validos")
    quit()

numero_ganador=random.choice(numeros)
color_ganador=random.choice(colores)

print(f"Ha tocado numero: {numero_ganador} y el color {color_ganador}")

if numero_ganador==numero_usuario and color_ganador==color_usuario:
    print("Has acertado el color y el numero")
elif numero_usuario==numero_ganador:
    print("Has adivinidado el numero")
elif color_ganador==color_usuario:
    print("Has adivinidado el color")
else:
    print("Has perdido")

