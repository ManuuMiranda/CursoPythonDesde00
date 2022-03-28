"""Teoría pura y dura"""
# Paradigmas de programación:
## Hay programacion orientada a procedimientos -> muy complicado y raro
## Hay programacion orientada a objetos -> estado, comportamiento (que puede hacer) y propiedades (atributos)


# Vocabulario:
## Clase: Modelo donde se redactan las |características comunes| de un grupo de objetos (chasis y 4 ruedas) -> coche

## Ejemplarizar/Instanciar/Objeto de clase: Ejemplar perteneciente a una clase (objetos del coche/ Citroen o seat)
### con sus características diferentes, cada coche sería una instancia diferente

## Modularización: Las diferentes clases que forman un programa, Clase 1 -> Clase 2 -> Clase 3, cada una independientes
### y reutilizables. Básicamente dividir el programa en módulos

## Encapsulación: Cada clase no sabe nada de las otras clases ni de su funcionamiento interno, clases protegidas
### del exterior del programa, las cosas se guardan dentro de la clase.
### Clase 1 no sabe nada de la Clase 2 pero están conectadas entre sí para que puedan funcionar como equipo

## Métodos de acceso: Sirven para conectar unas clases con otras para que funcionen como una unidad o equipo, tendrán
### acceso solo a algunas características de cada una de las clases.

## Objeto: Para poder acceder a las propiedas y comportamientos de un objeto se utiliza la nomenclatura del punto
### micoche.color = "rojo"/ micoche.arranca()


"""Empezamos con el código; aquí faltan matices, estado inicial del objeto y encapsulación"""

class Coche():  # Primera letra en mayus siempre en clases
    largoChasis = 250  # Primero se crean las propiedades
    anchoChasis = 120
    ruedas = 4
    enmarcha = False

    def arrancar(self):  # Ahora hay que crear los comportamientos, determinados por métodos, igual que this en Java y C
        self.enmarcha = True

    def estado(self):
        if self.enmarcha:  # Aunque no se ponga ==a True python lo entiendo como ==a True,es lo mismo =True q no ponerlo
            return "El coche está en marcha"
        else:
            return "El coche está parado"
# Por ahora solo hemos construido la clase, nada más

miCoche = Coche()  # Ya hemos creado el primer objeto, hemos instanciado la clase

print("El largo del coche es:", miCoche.largoChasis)
print("El coche tiene", miCoche.ruedas, "ruedas")
miCoche.arrancar()  # Sería lo mismo que poner miCoche.enmarcha=True
print(miCoche.estado())

# En este programa hemos introducido 4 propiedades y 2 comportamientos (metodos), en POO II profundizamos





