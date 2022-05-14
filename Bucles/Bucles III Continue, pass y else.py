for letra in "Python":
    print("Viendo la letra: " + str(letra))

for letra in "Python":
    if letra == "h":
        continue

    print("Viendo la letra: " + str(letra))

nombre = "Pildoras Informaticas"
print(len(nombre))  # El espacio en blanco cuenta como caracter

contador = 0

for i in nombre:
    if i == " ":  # El espacio en blanco ya no cuenta como caracter
        continue
    contador += 1

print(contador)

while True:
    pass  # Sirve para que no se ejecute al realizar el código


class Clase:
    pass  # Sirve para que no se ejecute al realizar el codigo, como pa completar mas tarde


def definicion():
    pass  # Sirve para que no se ejecute al realizar el codigo, como pa completar mas tarde



# Ejemplo:

email = input("Introduce tu email, por favor: ")

for i in email:
    if i == "@":
        caracter1 = True

        break;

else:
    caracter1 = False

print(caracter1)

