# Polimorfismo = Muchas formas
## Un objeto puede cambiar de forma dependiendo del contexto desde el que se utilice
## Ejemplo: Un coche pasa de ser a un camion o a una moto dependiendo del contexto

class Coche:
    def desplazamiento(self):  # Creamos un comportamiento
        print("Me desplazo utilizando cuatro ruedas")

class Moto:
    def desplazamiento(self):
        print(" Me desplazo utilizando dos ruedas")

class Camion:
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")

miVehiculo = Moto()
miVehiculo.desplazamiento()

miVehiculo2 = Coche()
miVehiculo2.desplazamiento()

miVehiculo3 = Camion()
miVehiculo3.desplazamiento()


class Coche:
    def desplazamiento(self):  # Creamos un comportamiento
        print("Me desplazo utilizando cuatro ruedas")


class Moto:
    def desplazamiento(self):
        print(" Me desplazo utilizando dos ruedas")


class Camion:
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")


def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


miVehiculo = Camion()  # Podríamos poner cualquier vehículo y luego con la función nos daría el desplazamiento

desplazamientoVehiculo(miVehiculo)