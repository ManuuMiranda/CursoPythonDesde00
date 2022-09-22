"""----------------Funciones Lambda (On demand, Online, On the go) ---------------"""


# Sirven para abreviar y hacer una sintaxis más ligera que ahorre tiempo
# Permite que funciones sencillas se puedan simplificar todavía más, si es compleja (bucles, condicionales) no se podrá


def area_triángulo(base, altura):
    return (base * altura) / 2


triangulo1 = area_triángulo(5, 7)
triangulo2 = area_triángulo(6, 8)

print(triangulo1)
print(triangulo2)

area_triángulo2 = lambda basex, alturax: (basex * alturax) / 2


triangulo3 = area_triángulo2(3, 4)
triangulo4 = area_triángulo2(4, 5)

print(triangulo3)
print(triangulo4)

al_cubo = lambda numero: pow(numero, 3)

print(al_cubo(5))  # Y se usa igual

destacar_valor = lambda comision: "¡ {} ! €".format(comision)

comision_ana = 15555

print(destacar_valor(comision_ana))


"""---------Función Filter y Utilidad (Programación Funcional != POO)-------------------------------------"""


def numeropar(num):
    if num % 2 == 0:
        return True


numeros = [17, 24, 7, 39, 8, 51, 92]

print(list(filter(numeropar, numeros)))


# Otra forma:

print(list(filter(lambda numero_par: numero_par % 2 == 0, numeros)))  # Nos ahorramos tener que crear la función


class Empleado:

    def __init__(self, nombre: str, cargo: str, salario: float):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"{self.nombre} que trabaja como {self.cargo} con un salario de {self.salario} €"
        # return "{} que trabaja como {} con un salario de {} €".format(self.nombre, self.cargo, self.salario)


lista_empleados = [

    Empleado('Juan', 'Director', 750000),
    Empleado('Ana', 'Presidente', 850000),
    Empleado('Antonio', 'Administrativo', 25000),
    Empleado('Sara', 'Secretaria', 27000),
    Empleado('Mario', 'Botones', 21000),

]

salarios_altos = filter(lambda empleado: empleado.salario > 50000, lista_empleados)

for i in salarios_altos:
    print(i)


"""-----------------Funciones Map---------------------------------------------------------------------------"""


# Aplica una función a cada elemento de una lista iterable (lista, tupla,...) Devuelve una lista con los resultados
# Susituiría el primer argumento de fiter por una función

lista_empleados2 = [

    Empleado('Juan', 'Director', 6700),
    Empleado('Ana', 'Presidente', 7500),
    Empleado('Antonio', 'Administrativo', 2100),
    Empleado('Sara', 'Secretaria', 2150),
    Empleado('Mario', 'Botones', 1800),

]


def calculocomision(empleadox):

    if empleadox.salario <= 3000:
        empleadox.salario = empleadox.salario*1.03
    return empleadox


lista_empleados3comision = map(calculocomision, lista_empleados2)

for i in lista_empleados3comision:
    print(i)

