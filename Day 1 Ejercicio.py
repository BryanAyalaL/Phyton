#Nivel 2

""""
Este es
un comentario
de n lineas
"""
#-----------------------------------------------------#
print(3+4)
print(3-4)
print(3*4)
print(10%4) #El modulo es el resto o resiudo de una division (en este caso es 2)
print(10/3)
print(3**4)
print(3/4)
print(10//3); """ Operador de piso dividido es el cociente
Aquí, 10 / 3 sería 3.333..., pero 10 // 3 solo devuelve la parte entera: 3."""


print("xyz")
print("xyz")
print("xyz")

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finlandia']))

#Nivel 3
print(type(20))
print(type(5.8))
print(type(3.4466556546548798567467596241622614624162416241))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finlandia']))
print(type({
'first_name':'Asabeneh',
'last_name':'Yetayeh',
'country':'Finland', 
'age':250, 
'is_married':True,
'skills':['JS', 'React', 'Node', 'Python']
}))
print(type(True))
print(type(["hola","esto es","una lista"]))

print(type(('Asabeneh', 'Pawel', 'Brook', 'Abraham', 'Lidiya')))
print(type({"hola","aqui no se puede repetir"}))

print ("Distancia euclidiana")
x1=float(input("Ingrese el valor de x1: "))
x2=float(input("Ingrese el valor de x2: "))
y1=float(input("Ingrese el valor de y1: "))
y2=float(input("Ingrese el valor de y2: "))

distancia=(((x2-x1)**2)+((y2-y1)**2))**(1/2)

print("La distancia euclidiana es de: ", distancia)