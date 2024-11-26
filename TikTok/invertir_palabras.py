def invertir_oracion(oracion):
    palabras= oracion.split()
    palabras_invertidad=palabras[::-1]
    return ' '.join(palabras_invertidad)

oracion="caulquier oracion"
resultado=invertir_oracion(oracion)
print(resultado)