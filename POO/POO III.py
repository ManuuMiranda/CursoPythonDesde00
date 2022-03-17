# Encapsulación de métodos, qué es, para qué sirve y por qué utilizarla

class Coche:  # Primera letra en mayus siempre en clases
    def __init__(self):  # Constructor de estado inicial
        self.largoChasis = 250  # Primero se crean las propiedades
        self.anchoChasis = 120
        self.__ruedas = 4  # Se pordía modificar pero habría que crear un método, si no, no
        self.__enmarcha = False  # Estado inicial, se puede modificar pero a través del método arrancar

    def arrancar(self, arrancamos: bool):
        self.__enmarcha = arrancamos
        if self.__enmarcha:
            chequeo = self.chequeo_interno()
        if self.__enmarcha and chequeo:
            return "El coche está en marcha"
        elif self.__enmarcha and chequeo == False:
            return "Algo va mal en el chequeo, no se puede arrancar"
        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene", self.__ruedas, "ruedas, un ancho de", self.anchoChasis, "y un largo de",
              self.largoChasis)

    def chequeo_interno(self):  # Por ahora es un método normal y corriente, no encapsulado
        print("Realizando chequeo interno")
        self.gasolina = "OK"
        self.aceite = "OK"
        self.puertas = "cerradas"

        if self.gasolina == "OK" and self.aceite == "OK" and self.puertas == "cerradas":
            return True
        else:
            return False


miCoche = Coche()

print(miCoche.arrancar(True))
miCoche.estado()

print("-----------A continuación creamos el segundo objeto---------------")

miCoche2 = Coche()
print(miCoche2.arrancar(False))
miCoche2.__ruedas = 2  # No nos deja porque es un valor encapsulado con los __
miCoche2.estado()

"""-----------Creamos el método encapsulado--------------"""


class Coche:
    def __init__(self):
        self.largoChasis = 250
        self.anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    def arrancar(self, arrancamos: bool):
        self.__enmarcha = arrancamos
        if self.__enmarcha:
            chequeo = self.__chequeo_interno()
        if self.__enmarcha and chequeo:
            return "El coche está en marcha"
        elif self.__enmarcha and chequeo == False:
            return "Algo va mal en el chequeo, no se puede arrancar"
        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene", self.__ruedas, "ruedas, un ancho de", self.anchoChasis, "y un largo de",
              self.largoChasis)

    def __chequeo_interno(self):
        print("Realizando chequeo interno")
        self.gasolina = "OK"
        self.aceite = "OK"
        self.puertas = "cerradas"

        if self.gasolina == "OK" and self.aceite == "OK" and self.puertas == "cerradas":
            return True
        else:
            return False


miCoche = Coche()

print(miCoche.arrancar(True))
miCoche.estado()
print(
    miCoche.__chequeo_interno())  # No tiene sentido porque al arrancar ya realiza el chequeo, veremos como encapsularlo

print("-----------A continuación creamos el segundo objeto---------------")

miCoche2 = Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()
print(miCoche.__chequeo_interno())  # No tiene sentido porque el coche está apagado y así no podría realizar chequeos
# Tras encapsular el método nos dará error el intento de impresión o no nos lo imprimirá directamente

# Para saber cuando encapsular o no un método solo hay que razonar si la clase o metodo lo necesita
