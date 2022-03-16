# Más aplicable cuando veamos POO, excepciones propias y tal

import math


def evaluaEdad(edad):
    if edad < 0:  # Raise sirve pa lazar tu propia excepción
        raise TypeError("Es imposible, no hay edades negativas")  # Lanzamiento de excepción
    if edad < 20:
        return "eres muy joven"
    elif edad < 40:
        return "eres joven"
    elif edad < 65:
        return "eres adulto"
    elif edad < 100:
        return "cuídate"


print(evaluaEdad(70))  # Problema si metiéramos una edad negativa, programa diría que eres muy joven
# Podríamos meter un if más o una excepción, aquí en verdad no tiene mucha utilidad pero ojo a sintaxis



def evaluaEdad(edad):
    if edad < 0:
        raise MiPropioError("Es imposible, no hay edades negativas")  # Nos dará doble error porque no definida la clase
    if edad < 20:
        return "eres muy joven"
    elif edad < 40:
        return "eres joven"
    elif edad < 65:
        return "eres adulto"
    elif edad < 100:
        return "cuídate"


import math

def calculaRaiz(num1):
    if num1 < 0:
        raise ValueError("El número no puede ser negativo")
    else:
        return math.sqrt(num1)


op1 = int(input("Introduce un numero: "))


try:
    print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print("Programa finalizado")

# Verdadera utilidad más adelante, al intentar conectar con bases de datos y otras cosas que escapan del control del
# programador.

