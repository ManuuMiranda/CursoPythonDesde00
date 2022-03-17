"""Ahora vamos a profundizar más en instancias u objetos creados"""


class Coche():  # Primera letra en mayus siempre en clases
    largoChasis = 250  # Primero se crean las propiedades
    anchoChasis = 120
    ruedas = 4
    enmarcha = False  # Estado inicial

    def arrancar(self, arrancamos: bool):
        self.enmarcha = arrancamos
        if self.enmarcha:  # Aunque no se ponga ==a True python lo entiendo como ==a True,es lo mismo =True q no ponerlo
            return "El coche está en marcha"
        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene", self.ruedas, "ruedas, un ancho de", self.anchoChasis, "y un largo de",
              self.largoChasis)


# Por ahora solo hemos construido la clase

miCoche = Coche()  # Ya hemos creado el primer objeto, hemos instanciado la clase

print(miCoche.arrancar(True))  # Sería lo mismo que poner miCoche.enmarcha=True
miCoche.estado()

print("-----------A continuación creamos el segundo objeto---------------")

miCoche2 = Coche()
print("El largo del coche es:", miCoche2.largoChasis)  # Característica en común
print("El coche tiene", miCoche2.ruedas, "ruedas")  # Característica en común
print(miCoche2.arrancar(False))  # Característica diferente
miCoche2.estado()

""" Todos los coches que creemos tendrán unas características comunes y estarán parados, estado inicial que se
    especifica con un constructor """


# Ahora construiremos uno con el ejemplo anterior

class Coche():  # Primera letra en mayus siempre en clases
    def __init__(self):  # Constructor de estado inicial
        self.largoChasis = 250  # Primero se crean las propiedades
        self.anchoChasis = 120
        self.__ruedas = 4  # Se pordía modificar pero habría que crear un método, si no, no
        self.__enmarcha = False  # Estado inicial, se puede modificar pero a través del método arrancar

    def arrancar(self, arrancamos: bool):
        self.__enmarcha = arrancamos
        if self.__enmarcha:  # Aunque no se ponga ==a True python lo entiendo como ==a True,es lo mismo =True q no ponerlo
            return "El coche está en marcha"
        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene", self.__ruedas, "ruedas, un ancho de", self.anchoChasis, "y un largo de",
              self.largoChasis)


# Por ahora solo hemos construido la clase

miCoche = Coche()  # Ya hemos creado el primer objeto, hemos instanciado la clase

print(miCoche.arrancar(True))  # Sería lo mismo que poner miCoche.enmarcha=True
miCoche.estado()

print("-----------A continuación creamos el segundo objeto---------------")

miCoche2 = Coche()
print(miCoche2.arrancar(False))  # Característica diferente
miCoche2.__ruedas = 2  # Cambiamos el estado inicial de las ruedas por 2, algo que realmente no se debería permitir
# aquí es donde entra la encapsulación, que se crea usando __ y no te deja cambiarlo aunque lo pongas
miCoche2.estado()

# También se pueden encapsular los métodos
