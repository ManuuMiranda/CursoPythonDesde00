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










