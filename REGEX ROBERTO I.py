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





