import re

""" re.search(pattern, string, flags=0) """

# Scanea sobre el string buscando la primera localización donde el patrón de regex produce un match y
# devuelve un match object correspondiente. Return None if no position in the string matches the pattern.

""" re.match(pattern, string, flags=0) """

# Si cero o más caracters al principio del string hacen match en el patrón regex,
# devuelve un match object correspondiente. Return None if the string does not match the pattern.

re.match("c", "abcdef")    # No match
re.search("c", "abcdef")   # Match

""" re.fullmatch(pattern, string, flags=0) """

# Si el string entero hace match con el patrón de regex, devuelve un match object correspondiente.
# Return None if the string does not match the pattern

""" re.split(pattern, string, maxsplit=0, flags=0) """

# Separa el string según el patrón de ocurrencias. Si los parentesis son usados en un patrón,
# entonces el texto de todos los grupos en el patrón son también devueltos como parte de una lista de resultados.

re.split(r'\W+', 'Words, words, words.')
re.split(r'(\W+)', 'Words, words, words.')
re.split(r'\W+', 'Words, words, words.', 1)
re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)

""" re.findall(pattern, string, flags=0) """

# El string es scaneado de izquierda a derecha y los matches los devuelve en el orden en el que los encuentra.
# Devuelve todos los matches no superpuestos de un patrón en el string, como una lista de strings.
# Los matches vacíos son incluidos en el resultado.

# Si uno o más grupos están presentes en el patrón, devuelve una lista de grupos,
# esta será una lista de tuplas si el patrón tiene más de un grupo.

""" re.sub(pattern, repl, string, count=0, flags=0) """

# Devuelve el string obtenido al remplazar gran parte de las ocurrencias no superpuestas del patrón
# en un string remplazado por el repl.
# Si no encuentra patrón el string devuelto no cambia, el repl puede ser un string o una función.
# Si repl es una función, es llamada para cada ocurrencia no superpuesta del patrón.



"""
Match objects always have a boolean value of True. Since match() and search() return None when there is no 
match, you can test whether there was a match with a simple if statement.
Match objects support the following methods and attributes:

Match.group([group1, ...]) Returns one or more subgroups of the match. I

Match.groups(default=None)¶ Return a tuple containing all the subgroups of the match, from 1 up to 
however many groups are in the pattern. 

Match.span([group]) For a match m, return the 2-tuple (m.start(group), m.end(group)). 
"""
