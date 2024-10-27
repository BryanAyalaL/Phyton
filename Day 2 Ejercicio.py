nombre="bryan"
apellido="Londoño"
nombre_completo=nombre+apellido
pais="Colombia"
ciudad="Medellín"
edad=18
año=2024
estado_civil=False
es_verad=True
is_light_on=False
x,y,z="x","y","z"



print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(año))
print(type(estado_civil))
print(type(es_verad))
print(type(is_light_on))
print(type(x),type(y),type(z))


print(len(nombre_completo))

numero_uno=5
numero_dos=4
sumar=numero_uno+numero_dos
restar=numero_dos-numero_uno
multiplicar=numero_dos*numero_uno
dividir=numero_uno/numero_dos
resto=numero_dos%numero_uno
esp=numero_uno**numero_dos
dividir_piso=numero_uno//numero_dos
# Imprimir resultados
print("Suma:", sumar)
print("Resta:", restar)
print("Multiplicación:", multiplicar)
print("División:", dividir)
print("Resto:", resto)
print("Exponenciación:", esp)
print("División entera:", dividir_piso)


radio_circulo=30 #metros
pi=3.14
area_circulo=pi*radio_circulo**2
circuferencia_circulo=2*pi*radio_circulo
radio_circulo=int(input("Introduzca el radio del circulo"))
area_circulo=pi*radio_circulo**2
circuferencia_circulo=2*pi*radio_circulo
print("Este es el area del circulo: ",area_circulo, "Este es la circunferencia del circulo: ",circuferencia_circulo)


# Usando la función input() para obtener datos del usuario
nombre = input("Por favor ingresa tu nombre: ")
apellido = input("Por favor ingresa tu apellido: ")
pais = input("Por favor ingresa tu país: ")
edad = int(input("Por favor ingresa tu edad: "))

# Mostrando los valores ingresados
print("\nInformación del usuario:")
print("Nombre:", nombre)
print("Apellido:", apellido)
print("País:", pais)
print("Edad:", edad)
