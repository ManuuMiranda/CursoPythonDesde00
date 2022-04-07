"""Funciones Match() y Search()"""
# La función match busca coincidencias en un patron de búsqueda al comienzo de una cadena de texto, siempre al comienzo
## La función match distingue entre mayus y minus, a no ser que
## pongamos un tercer parámetro re.IGNORECASE o lower()/ upper()

# La función search busca en toda la cadena de texto si el patrón de búsqueda se encuentra o no

# Ejemplos con match:
print("Ejemplos con match:")

import re

nombre1 = "Sandra López"

nombre2 = "Antonio Gómez"

nombre3 = "María López"

if re.match("Sandra", nombre1):
    print("Nombre Encontrado")
else:
    print("Nombre No Encontrado")


# Ejemplo con comodín del punto:
print("Ejemplo con comodín del punto:")

import re

nombre1 = "Jara López"

nombre2 = "Antonio Gómez"

nombre3 = "Lara López"

if re.match(".ara", nombre1, re.IGNORECASE):  # Pongamos nombre 1 o nombre 2, va a encontrar el nombre
    print("Nombre Encontrado")
else:
    print("Nombre No Encontrado")


# Ejemplo con cadenas con números:
print("Ejemplo con cadenas con números:")

import re

cadena1 = "Jara López"

cadena2 = "546546546"

cadena3 = "a54654654"

if re.match("\d", cadena3, re.IGNORECASE):  # \d busca usando funcion match si la cadena empieza o no por un número
    print("Número Encontrado")
else:
    print("Número No Encontrado")


# Ejemplo con search:
print("Ejemplo con search:")

import re

nombre1 = "Jara López"

nombre2 = "Antonio Gómez"

nombre3 = "Lara López"

if re.search("López", nombre1):
    print("Nombre Encontrado")
else:
    print("Nombre No Encontrado")

# Ejemplo con cadena larga:
print("Ejemplo cadena larga:")

import re

codigo1 = "rebkjbwvewi71"

codigo2 = "weljgngsln71vsjbvljb"

codigo3 = "rouwvbow"

if re.search("71", codigo1):
    print("Código Encontrado")
else:
    print("Código No Encontrado")