# IF:

def evaluacion(nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "suspenso"
    return valoracion


print(evaluacion(6))
print(evaluacion(4))

## Ahora pidiendonos que introduzcamos la nota por teclado

print("Programa de evaluación de notas de alumnos")

nota_alumno = input("Introduce la nota del alumno: ")


def eval(nota: int):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "suspenso"
    return valoracion


print(eval(int(nota_alumno)))

# IF, else y elif:
# else = y si no es verdad
# elif es como varios else

print("Verificación de acceso")

edad_usuario = int(input("Introduzca su edad:"))

if edad_usuario < 18:
    print("No puedes pasar")
else:
    print("Pase")

print("El programa ha finalizado")


print("Verificación de acceso 2")

edad_usuario = int(input("Introduzca su edad:"))

if edad_usuario < 18:
    print("No puedes pasar")
elif edad_usuario > 80:
    print("Edad incorrecta")
else:
    print("Pase")

print("El programa ha finalizado")

print("Verificación de acceso 3")

nota_alumni = int(input("Introduzca su nota:"))

if nota_alumni < 5:
    print("Insuficiente")
elif nota_alumni < 6:
    print("Suficiente")
elif nota_alumni < 7:
    print("Bien")
elif nota_alumni < 9:
    print("Notable")
elif nota_alumni <= 10:
    print("Sobresaliente")
else:
    print("Vas loco")

print("El programa ha finalizado")

# Parte 3

edad = 7
if edad < 100:
    print("Edad es correcta")
else:
    print("Edad incorrecta")


edad3 = -7
if edad3 < 100:
    print("Edad es correcta")
else:
    print("Edad incorrecta")


edad4 = -7
if 0< edad4 < 100:
    print("Edad es correcta")
else:
    print("Edad incorrecta")

# AND y OR:
## AND = y si además
## OR = o si no

# Distancia > 40km
# Nº Hermanos > 2
# Salario familiar <= 20000

print("Programa de becas")

dist_escuela = int(input("Introduce la dist a la escuela:"))
print(dist_escuela)

num_hermanos = int(input("Introduce el nº de hermanos en el centro:"))
print(num_hermanos)

salario_familiar = int(input("Introduce el salario familiar:"))
print(salario_familiar)

if dist_escuela > 40 and num_hermanos > 2 and salario_familiar <= 20000:
    print("Beca")
else:
    print("No beca")


# así tiene más sentido

print("Programa de becas")

dist_escuela = int(input("Introduce la dist a la escuela:"))
print(dist_escuela)

num_hermanos = int(input("Introduce el nº de hermanos en el centro:"))
print(num_hermanos)

salario_familiar = int(input("Introduce el salario familiar:"))
print(salario_familiar)

if dist_escuela > 40 and num_hermanos > 2 or salario_familiar <= 20000: # Si tiene salario bajo cuenta tb
    print("Beca")
else:
    print("No beca")

# Por último:

print("Asignaturas optativas")

print("Asignaturas optativas: Informática - Pruebas de Software - Usabilidad")

asignatura = input("Escribe la asignatura escogida:")

if asignatura in ("Informática", "Pruebas de Software", "Usabilidad"):
    # Siempre con comas aunque sean numéricos, comillas solo en str
    print("Asignatura elegida" + asignatura) # No se pone función str pq ya es un str
else:
    print("La asginatura elegida no está contemplada")

# Python distingue mayus y minus, pa que de igual en el programa usamos lower() pa minus y upper() pa mayus

print("Asignaturas optativas")

print("Asignaturas optativas: Informática - Pruebas de Software - Usabilidad")

optativa = input("Escribe la asignatura escogida:")

asignatura = optativa.lower() # tb se podría poner upper() y ponerlo to en mayus  en el if de abajo

if asignatura in ("informática", "pruebas de software", "usabilidad"):
    # Siempre con comas aunque sean numéricos, comillas solo en str
    print("Asignatura elegida" + asignatura) # No se pone función str pq ya es un str
else:
    print("La asginatura elegida no está contemplada")


