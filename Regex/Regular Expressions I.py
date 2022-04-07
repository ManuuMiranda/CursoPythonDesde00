import re

cadena = "Vamos a aprender expresiones regulares"

print(re.search("aprender", cadena))
print(re.search("aprenderrrrr", cadena))  # Si no encuentra el texto devolverá None

textoabuscar = "aprender"

if re.search(textoabuscar, cadena) is not None:
    print("Text found")
else:
    print("Text not found")

# Otro ejemplo:

import re

cadena = "Vamos a aprender expresiones regulares"
textoabuscar = "aprender"

textoEncontrado = re.search(textoabuscar, cadena)

print(textoEncontrado)
print(textoEncontrado.start())  # Dice el caracter donde comienza lo que buscamos(texto)
print(textoEncontrado.end())  # Dice en que caracter finaliza lo que buscamos
print(textoEncontrado.span())  # Dice donde empieza y donde acaba lo que buscamos

# Con una cadena más larga

import re
print("Ejemplo con Findall:")

cadena = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"
textoabuscar = "Python"

print(re.findall(textoabuscar, cadena))  # Devuelve los strings que han coincidido con la búsqueda
print(len(re.findall(textoabuscar, cadena)))


"""Expresiones Regulares para confeccionar patrones de búsqueda"""
# Caracteres comodín o metacaracteres

import re

lista_nombres = ['Ana Gómez', 'María Martín', 'Sandra López', 'Santiago Martín', 'Sandra Fernández']

print("Ejemplo con ^:")
for elemento in lista_nombres:
    if re.findall('^Sandra', elemento):  # El ^ sirve para ver qué elemento empieza por lo que pongas a continuación
        print(elemento)

print("Ejemplo con $:")
for elemento in lista_nombres:
    if re.findall('Martín$', elemento):  # El $ sirve para ver qué elemento acaba por lo que pongas antes
        print(elemento)

# Otro ejemplo con dominios:

import re

lista_dominios = ['http://pildorasinformaticas.es',
                  'ftp://pildorasinformaticas.es',
                  'http://pildorasinformaticas.com',
                  'ftp://pildorasinformaticas.com']  # La gracia es hacerlo con muchos más

for element in lista_dominios:
    if re.findall('es$', element):
        print(element)

for element in lista_dominios:
    if re.findall('^ftp', element):
        print(element)


# Si pongo [sfg] entre corchetes, se buscará si en el texto están los caracteres, sin importar el orden

import re

lista_dominios2 = ['http://informaticaespaña.es',
                  'http://pildorasinformaticas.es',
                  'ftp://pildorasinformaticas.com']

for elementx in lista_dominios2:
    if re.findall('[ñ]', elementx):
        print(elementx)


# Ejemplo con variaciones:
print('Ejemplo Variaciones:')

import re

lista_nombres2 = ['hombres', 'mujeres', 'niños', "niñas"]

for i in lista_nombres2:
    if re.findall('niñ[oa]', i):  # Así encuentra niños y niñas, gracias a usar [], corchetes
        print(i)


# Ejemplo acentos:
print('Ejemplo Acentos:')

import re

lista_nombres3 = ['hombres', 'mujeres', 'camión', 'camion']

for x in lista_nombres3:
    if re.findall('cami[oó]n', x):
        print(x)


# Ejemplo Rangos:
print('Ejemplo Rangos:')

import re

lista_nombres4 = ['Ana', 'Pedro', 'María', 'Rosa', 'Sandra', 'Celia']

for v in lista_nombres4:
    if re.findall('[o-t]', v):
        """Devuelve todos los nombre en cuyo interior hay un rango de letras comprendido entre o y t,
        distingue mayus y minus"""
        print(v)


# Ejemplo Rangos 2:

print('Ejemplo Rangos:')

import re

lista_nombres4 = ['Ana', 'Pedro', 'María', 'Rosa', 'Sandra', 'Celia']

for v in lista_nombres4:
    if re.findall('^[o-t]', v):  # No saldrá nada, porque busca los que empiecen por letras de ese rango
        print(v)

for v in lista_nombres4:
    if re.findall('^[O-T]', v):  # Si devuelve porque diferencia entre mayus y minus
        """Devuelve todos los nombre en cuyo interior hay un rango de letras comprendido entre o y t,
        distingue mayus y minus, al ponerlo en mayus si devuelve un resultado """
        print(v)

for v in lista_nombres4:
    if re.findall('[o-t]$', v):  # Solo saldrá pedro
        print(v + " \nFin del ejercicio")


