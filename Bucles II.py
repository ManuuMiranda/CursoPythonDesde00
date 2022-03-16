# Particularidad del while: No sabemos cuántas veces se va a ejecutar, error hacer que sea infinito muchas veces

# Se traduce a un mientras
# No se debe crear un bucle while con una condición que jamás deje de ser verdadera, a no ser que se quiera un bucle inf

import math

i = 1

while i <= 10:
    print("Ejecución" + str(i))  # No es del to correcto, bucle infinito

print("Termina la ejecución")

import math

i = 1

while i <= 10:
    print("Ejecución" + str(i))  # aquí no se ve caracter o naturaleza indeterminada
    i = i +1  # contador pa que el bucle no sea infinito

print("Termina la ejecución")

# Programa con edades:

edad = int(input("Introduce edad: "))

while edad <= 0:
    print("Has introducido una edad no válida, prueba otra vez")
    edad = int(input("Introduce edad: "))

print("Gracias, pase")
print("Edad del aspirante " + str(edad))

# Programa con edades 2 (con mas sentido):

edad = int(input("Introduce edad: "))

while edad <= 5 or edad > 80:
    print("Has introducido una edad no válida, prueba otra vez")
    edad = int(input("Introduce edad: "))

print("Gracias, pase")
print("Edad del aspirante " + str(edad))

# Como salir de un bucle infinito/ como hacer que un bucle jamás sea infinito por mucho que se empeñe el usuario

print("Programa de calculo de raíz cuadrada")

numero = int(input("Introduce un numero: "))
intentos = 0

while numero < 0:
    print("No se puede hallar la raiz de un numero negativo")

    if intentos == 2:
        print("has consumido demasiados intentos, el programa ha finalizado")
        break;

    numero = int(input("Introduce un numero: "))
    if numero <0:
        intentos = intentos + 1

if intentos < 2:
    solucion = math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + "es" + str(solucion))