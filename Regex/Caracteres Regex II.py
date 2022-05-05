import re

"""                       ESPECIFICACIONES 2:
{m} especifica que exactamente m copias del anterior RE deberán hacer match, 
menos matches darán lugar a que el RE entero no haga match. 

Por ejemplo, a{6} hará match exactamente a 6 caracteres 'a' pero no 5.

{m,n} dará resultado a un match de m a n repeticiones del anterior RE, 
intentando hacer un match de las máximas repeticiones possibles. 

Por ejemplo, a{3,5} hará match de 3 a 5 characters 'a'.  
Omitir m specifica un límite inferior a cero, y omitir n specifica un limite infinito. 

Por ejemplo, a{4,}b hará match con 'aaaab' o con mil 'a's seguidas por una 'b', pero no 'aaab’.
No se debe omitir la coma o el modifier se confundirá con la forma descrita anteriormente.
"""

re.match('a{2,3}', 'abc dat')
re.match('a{2,3}', 'abc daat')
re.match('a{2,3}', 'aabc daaat')
re.match('a{2,3}', 'aabc daaaat')

re.match('a{3,5}', 'aaaaaa')  # Ojo
re.match('a{3,5}?', 'aaaaaa')  # Ojo

"""                    FUNCIONES DEL \:
1º. Escapa los caracteres especiales, permite hacer match con caracteres como '*', '?' y más.

2º. Señala una sequencia especial:
    Regex Pipe (A|B): Crea una regex que hará match con A o B, prueba de izquierda a derecha.
                      Cuando un patrón casa por completo, esa rama es aceptada, non-greedy.       
    (...) Hace match con cualquier regex dentro del paréntesis e indica el inicio y fin de un grupo.
                      Los contenidos de un grupo pueden ser retirados después de realizar un match, 
                      y puede dar match después en el string con el \número de secuencia especial, descrito debajo.
                      Por ejemplo, (.+) \1 hace match de 'the the' or '55 55', pero no 'thethe'.
    Si lo sigue un dígito de ASCII como \1 -> Representa al grupo 1
    Si lo sigue una letra de ASCII como \w -> Entonces representa una secuencia especial, como cualquier palabra.
"""

m = re.match(r'(.*bc)def', 'abcdef')
m.group(1)
m = re.match(r'(.+) \1', 'the the')
m.group(1)
m = re.match(r'(.+) \1', 'thethe')
m is None

"""
•\w Matches alphanumeric characters, which means a-z, A-Z, and 0-9. It also matches the underscore, _.
•\W Matches non-alphanumeric characters
•\d Matches digits, which means 0-9.
•\D Matches any non-digits.
•\s Matches whitespace characters, which include the \t, \n, \r, and space characters.
•\S Matches non-whitespace characters.
"""

"""
·\d Matches any Unicode decimal digit 
·\D Matches any character which is not a decimal digit. 
·\w Matches Unicode word characters;
·\s Matches Unicode whitespace characters (which includes [ \t\n\r\f\v]
·\S Matches any character which is not a whitespace character.
"""