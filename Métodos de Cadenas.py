# En strings
## upper() -> convierte en mayus todas las letras de un string/lower() -> convierte en minus todas las letras de string
## capitalize() -> en un string pone la 1era letra en mayus

## count() -> contar cuantas veces aparece una letra o una cadena de caracteres dentro de una frase o texto

## find() -> representa el índice/posicion en el cual aparece un caracter o grupo de caracteres en un texto

## isdigit() -> devuelve un Bool de si es un digito el valor introducido o no

## isalum() -> devuelve un Bool de si es alfanumérico o no el valor introducido

## isalpha() -> comprueba si hay solo letras, los espacios no cuentan

## split() -> separa por palabras utilizando espacios

## strip() -> borra los espacios sobrantes al principio y al final

## replace() -> cambia una palabra o una letra por otra

## rfind() -> representa el índice de un caracter contando desde atrás, como el find pero al revés (reversefind)


""" Interesante entrar en página web de documentación de python """

# Ejemplos con código

nombreUsuario = input("Introduce tu nombre de Usuario")

print("El nombre es", nombreUsuario.upper())

print("El nombre es:", nombreUsuario.lower())

print("El nombre es:", nombreUsuario.capitalize())  # Funciona pongas to en mayus o to en minus


edad = input("Introduce tu edad:")

print(edad.isdigit())

if int(edad) < 18:
    print("No puede pasar")
else:
    print("Puede pasar")

# Para que no se caiga si pones un str

edad = input("Introduce tu edad:")

while edad.isdigit() == False:
    print("Introduce un valor numérico")
    edad = input("Introduce tu edad:")

if int(edad) < 18:
    print("No puede pasar")
else:
    print("Puede pasar")

# Último ejercicio

"""Crea un programa que pida introducir una dirección de email por teclado. El programa
debe imprimir en consola si la dirección de email es correcta o no en función de si esta
tiene el símbolo ‘@’. Si tiene una ‘@’ la dirección será correcta. Si tiene más de una o
ninguna ‘@’ la dirección será errónea. Si la ‘@’ está al comienzo de la dirección de email
o al final, la dirección también será erronea"""

mailUser = input("Introduce tu email:")

arroba = mailUser.count('@')

if arroba != 1 or mailUser.rfind('@') == len(mailUser)-1 or mailUser.find('@') == 0:
    print("Mail incorrecto")
else:
    print("Mail correcto")


