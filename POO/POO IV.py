""" Teoría """
# Herencia:
## Qué es, para qué sirve y cómo hacer que las clases hereden

# Translada comportamiento de herencia entre personas a código de programación: Abuelo -> Padre -> 3 Hijos cada uno con
## sus bienes y cosas. Pa heredar hay que fallecer, y los bienes pasan al descendiente, y asi to el rato

## En progra se sustituyen a estas personas por clases: Clase padre o super clase -> Clase padre y subclase y superclase
## de las clases siguientes.

# Sirve para reutilizar el código en caso de crear objetos similares, en vez de crear class Coche, crear to tipo de
## vehículos que tienen sus características similares (marca, modelo, etc...) y comportamientos comunes (arrancar, etc)
## y luego con sus características y comportamientos únicos

## Estas caracteristicas y comportamientos comunes se pondrían en una clase padre o superclase.


"""Empezamos"""


class Vehiculos:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self.__enmarcha = False
        self.__acelera = False
        self.__frena = False

    def arrancar(self):
        self.__enmarcha = True

    def acelerar(self):
        self.__acelera = True

    def frenar(self):
        self.__frena = True

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn Marcha:", self.__enmarcha, "\nAcelerando:",
              self.__acelera, "\nFrenando:", self.__frena)


class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"


class Moto(Vehiculos):
    hcaballito = ""

    def caballito(self):  # Cómo hacemos para que salga en el estado? Con su propio método de estado
        self.hcaballito = "Voy haciendo el caballito"

    def estado(self):
        print("Marca:", self.marca, "\n Modelo", self.modelo, "\n", self.hcaballito)
        # Si quisieramos poner __enmarcha, __frena y __acelera, tendríamos que quitar las __ que lo protegen, yo no
        # lo voy a hacer así para caer en la cuenta de ello


class VElectricos(Vehiculos):  # Ponemos vehículos entre paréntesis para añadir el super
    def __init__(self, marca:str, modelo : str):
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True


# Podríamos crear una subclase de moto quad también, heredaría el caballito y el metodo estado de moto

miMoto = Moto("Honda", "CBR")

miMoto.caballito()  # Si no ejecutaramos esta línea saldría una cadena de texto vacía

miMoto.estado()  # Llamamos al método estado de la clase moto, no de la clase vehículo

print("---------Continuamos-------------")

miFurgoneta = Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

miFurgoneta.carga(True)  # Por como hemos definido el metodo carga no nos saldrá el texto sin un print
print(miFurgoneta.carga(True))


class BicicletaElectrica(VElectricos, Vehiculos):  # Doble herencia/multiple, con métodos y propiedades de ambas clases
    pass


#miBici = BicicletaElectrica()  # Coge los parámetros de la primera clase que cojas, en este caso VElecticos, y por ello
# no ponemos argumentos dentro, si lo hicieramos al reves habría que poner marca y modelo
"""Básicamente cogerá el método init de la primera clase, VElectricos, podríamos repetir el init de Vehiculos tb para
   solucionarlo pero no es muy elegante, mejor utilizar funciñon super"""
# Con el super ya podemos poner marca y modelo

miBici = BicicletaElectrica("Orbea", "Rallon")