import re
pattern = '^a...s$'  # Primero se el patrón
test_string = 'abyss'
result = re.match(pattern, test_string)  # Devuelve un match si ha encontrado algo y un None si no ha encontrado nada

"""                         ESPECIFICACIONES MÁS TÍPICAS
[] Especifica una serie de caracteres con los que queramos hacer un match, [amk] encontrará 'a', 'm' o 'k'
Puede dar 1 match, 2 o los que sea.
[a-e] = [abcde] / [1-4] = [1234] / [^abc] = Todos los caraceres menos a, b o c / [^0-9] = Todoss excepto los numéricos
[0-39] = [01239]
. simboliza cualquier caracter menos una nueva línea.
.. = 2 caracteres
^a simboliza que tiene que estar al principio y a$ simboliza que tiene que estar al final
"""

"""
* hace que se encuentren 0 o más repeticiones de los caracteres puestos antes, hasta el máximo de repeticiones que haya.
ab* hará match con 'a', 'ab' o 'a' seguida de cualquier número de 'b's
"""

re.match('ma*n', 'mn')
re.match('ma*n', 'man')
re.match('ma*n', 'main')
re.match('ma*n', 'mannnnn')  # Ojo
re.match('ma*n', 'woman')

"""
+ hace que se encuentren 1 o más repeticiones de los caracteres puestos antes.
ab+ hará match con 'a' seguido de número distinto de 0 de 'b's y no hará match solo con 'a'
"""

re.match('ma+n', 'mn')
re.match('ma+n', 'man')
re.match('ma+n', 'maaaan')
re.match('ma+n', 'main')
re.match('ma+n', 'woman')

"""
? hace que encuentren 0 o 1 repeticiones de los caracteres puestos antes.
ab? hará match con 'a' o 'ab'
"""

re.match('ma?n', 'mn')
re.match('ma?n', 'man')
re.match('ma?n', 'maaan')
re.match('ma?n', 'mainn')
re.match('ma?n', 'woman')

"""
'*', '+', and '?' son ambiciosos y hacen match con todo el texto que puedan pero a veces es un comportamiento no deseado
Si <.*> hace match con '<a> b <c>',  hará match con todo el string, y no solo con '<a>’. 

Añadir ? después del qualifier hace el match de forma no ambiciosa o mínima; hará match con el 
mínimo número de caracteres possible.
Usar el match <.*?> hará match solo con '<a>'.

SEGUIREMOS CON ESTO EN LA 2da PARTE
"""

