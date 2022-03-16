# Función tradicional VS Generador

# Generador se acaba con yield no con return, aunque puede llevar ambas

# Función construye y devuelve toda la lista de una
# Generador construye objeto iterable que nos va a devolver, de uno en uno según control de flujo
# Cada vez que lo llamas genera, la función lo tira de golpe

# Funciones consumen más recursos y Generador menos, mejor para acceder solo a un elemento de la lista

# Generadores más utiles con listas de valores infinitos, entre otras cosas.


# Sintaxis:

## Función:

def generaPares(limite):
    num = 1
    miLista = []
    while num < limite:
        miLista.append(num*2)
        num += 1
    return miLista


print(generaPares(10))

## Generador:

def generaPares(limite):
    num = 1

    while num < limite:
        yield num*2  # Yield anida los elementos
        num += 1


devuelvepares = generaPares(10)  # guarda en variable objeto el objeto iterable que devuelve la función

for i in devuelvepares:
    print(i)
# Ejemplo pedagógico, aquí no hay eficiencia


# Si solo quisiera imprimir los 3 primeros elementos


def generaPares(limite):
    num = 1
    while num < limite:
        yield num*2
        num += 1


devuelvepares = generaPares(10)  # guarda en variable objeto el objeto iterable que devuelve la función

print(next(devuelvepares))

print("Aqui podria ir mas codigo...")

print(next(devuelvepares))
# Entre llamada y llamada el objeto generador entra en estado de suspension/standby, + eficiente

print("Aqui podria ir mas codigo...")

print(next(devuelvepares))

# En lista tradicional habría que crear la lista completa y luego imprimir los 3 primeros valores, ocupando mas espacio



# Función yield from,  simplifica codigo de los generadores en caso de utilizar bucles anidados ( como for )
## Para acceder a uno de los elemntos anidados y su interior o subelementos parecido a un array de 2 dimensiones

def devuelve_ciudades(*ciudades):  # El * sirve pa indicar al programa que va a recibir un número indeter de elementos
                                   # en forma de tupla
    for elemento in ciudades:
        #for subElemento in elemento:
        yield from elemento

ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))


# Sin yield from:

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield elemento

ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))




