# Pueden ser determinados (se sabe número de veces a ejecutar) o indeterminados (no se sabe o dependerá o infinito):

for i in [1, 2, 3]:
    print("Hola")

for i in ["primavera", "verano", "otoño", "invvierno"]:
    print("Hola")

for i in ["primavera", "verano", "otoño", "invvierno"]:  # La variable se puede llamar i o como quieras
    print(i)

for i in ["Pildoras", "Informaticas", 3]:
    print("Hola")

for i in ["Pildoras", "Informaticas", 3]:
    print("Hola", end="")

for i in ["Pildoras", "Informaticas", 3]:
    print("Hola", end=" ")  # Lo hacemos para que tenga un espacio

for i in "juanm@gmail.com":  # imprime tantas veces como carácteres tenga el string
    print("Hola", end="")

# Codigo nuevo #

email = False

for i in "juanm@gmail.com":  # el for va tomando todos los valores del string hasta que termine de recorrer el string
    if i == "@":  # cuando el for llega al @ se cambia el valor de la variable a True, habiéndola iniciado en False
        email = True  # si no hay @ esta linea no se lee y por tanto el email es False como declarada al ppio del codigo

if email == True:
    print("el mail es correcto")
else:
    print("el mail es incorrecto")

# Con un input

email = False
miEmail = input("Introduce tu dirección de mail: ")

for i in miEmail:
    if i == "@":
        email = True

if email == True:
    print("Mail correcto")
else:
    print("Mail incorrecto")

# Con un contador

contador = 0
miEmail = input("Introduce tu dirección de mail: ")

for i in miEmail:
    if i == "@" or i == ".":
        contador = contador + 1

if contador == 2:
    print("Mail correcto")
else:
    print("Mail incorrecto")

# Tipo range

for i in range(5):  # Imprime 5 elementos: 0,1,2,3,4
    print("Hola")

for i in range(5):  # Imprime 5 elementos: 0,1,2,3,4
    print(i)  # Imprimirá los nºs 0,1,2,3,4

for i in range(5):
    print(f'Valor de la variable {i}')  # Si no pusieramos la f lo imprimiría como str 5 veces

for i in range(5, 50, 3):
    print(f'Valor de la variable {i}')

len("juan")  # Función len en str devuelve el nº de caracteres (4 en este caso)

# Último ejercicio:

valido = False

email = input("Introduce tu mail: ")

for i in range(len(email)):
    if email[i] == "@": 
        valido = True

if valido == True:
    print("Buen mail")
else:
    print("Mal mail")
