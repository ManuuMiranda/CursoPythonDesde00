# Las excepciones son errores que ocurren durante la ejecución de un programa, sintaxis correcta pero durante
## ejecución ha ocurrido "algo inesperado", catastrófico en programas grandes
## Para que se ejecuten las lineas que van despues de ese error

# Construcción:
#try-except-else-finally, todas opcionales menos el try.

def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplica(num1, num2):
    return num1 * num2


def divide(num1, num2):  # Si dividiéramos entre 0 el resto del programa cae (se para la ejecución),
    # por eso son buenas las excepciones

    try:
        return num1 / num2
    except ZeroDivisionError:  # Excepción para que el programa no se caiga si se divide entre 0
        print("No se puede dividir entre 0")
        return "Operación erronea"


try:
    op1 = int(input("Introduce el primer numero: "))
    op2 = int(input("Introduce el segundo numero: "))

except ValueError:
    print("Los valores introducidos no sonn correctos")

operacion = input("Introduce la operación a realizar (suma, resta, multiplica, divide): ")

if operacion == "suma":
    print(suma(op1, op2))
elif operacion == "resta":
    print(resta(op1, op2))
elif operacion == "multiplica":
    print(multiplica(op1, op2))
elif operacion == "divide":
    print(divide(op1, op2))
else:
    print("Operación no contemplada")

print("Operación ejecutada. Continuación de ejecución del programa")




# Ahora con más sentido, sin que pida "operación a realizar" tras poner un string (value error)

def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplica(num1, num2):
    return num1 * num2


def divide(num1, num2):  # Si dividiéramos entre 0 el resto del programa cae (se para la ejecución),
    # por eso son buenas las excepciones
    try:
        return num1 / num2
    except ZeroDivisionError:  # Excepción para que el programa no se caiga si se divide entre 0
        print("No se puede dividir entre 0")
        return "Operación erronea"


while True:
    try:
        op1 = int(input("Introduce el primer numero: "))  # Si op1 y op2 son correctos saldrá del bucle sin pasar por
        op2 = int(input("Introduce el segundo numero: "))  # el except, si es valor erroneo saltará al except, y pide op
        break  # Si no no saldríamos nunca del bucle, no se leera línea si entra en el except y por ello pide op again
        # así hasta que pongas bien los valores

    except ValueError:
        print("Los valores introducidos no son correctos, intentalo de nuevo")

operacion = input("Introduce la operación a realizar (suma, resta, multiplica, divide): ")

if operacion == "suma":
    print(suma(op1, op2))
elif operacion == "resta":
    print(resta(op1, op2))
elif operacion == "multiplica":
    print(multiplica(op1, op2))
elif operacion == "divide":
    print(divide(op1, op2))
else:
    print("Operación no contemplada")

print("Operación ejecutada. Continuación de ejecución del programa")
