# Función chr() nos dice que posición ocupa un número en el lenguaje unicode '97' = 'a'
chr(97)
# Función ord() nos dice que número ocupa una letra en el lenguaje unicode 'a' = '97', solo una vez por caracter 'ab' no
ord('a')

# Suma de strings y accesos
a = 'abc'
d = 'def'
abcdef = a+d  # Une 2 strings en uno
abcdef[1:5]

# Separar un string con .split()
title = 'The Good, The Bad, and the Ugly'
print(title.split(' '))

# Reemplazamiento
welcome_message = 'Hello World!'
welcome_message.replace("Hello", "Goodbye")

# Encontrar substrings
'Edward Alun Rawlings'.find('Alun')
Ed = 'Edward Alun Rawlings'  # Nos dirá la posición en la que empieza el substring
Ed.find('Alun')

# Unir elementos separados por coma en una lista
num_list = ['1', '2', '3', '4']
separator = ', '
separator.join(num_list)
