
def divide():
    try:
        op1 = (float(input("Introduce el primer número: ")))
        op2 = (float(input("Introduce el segundo número: ")))

        print("La división es: " + str(op1 / op2))

    except ValueError:
        print("El valor introducido es erróneo")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")

    finally:  # En este caso no sirve, pero sería para que se ejecutase siempre la línea de codigo dentro
        print("Calculo finalizado")


divide()


# Otra opción más genérica y menos recomendada:

def divide():
    try:
        op1 = (float(input("Introduce el primer número: ")))
        op2 = (float(input("Introduce el segundo número: ")))

        print("La división es: " + str(op1 / op2))

    except:  # El programa no cae pero usuario no sabe por qué, captura excepcion general
        print("Ha ocurrido un error")

    print("Calculo finalizado")


divide()



# Otro ejemplo:

def divide():
    try:  # Intenta hacer el try y si hay un error no se captura na pero programa no cae y se ejecuta el finally
        op1 = (float(input("Introduce el primer número: ")))
        op2 = (float(input("Introduce el segundo número: ")))

        print("La división es: " + str(op1 / op2))

    finally:  # En este caso si sirve, si lo quitamos da error y el print de después no se ejecuta
        print("Calculo finalizado")

# Necesitaremos un finally o un except después del try para que tenga sentido el mismo try