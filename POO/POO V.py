# Función super():
## Sirve para llamar al método de la clase padre.

# Principio de sustitución:Aplicar los términos de:" es siempre un/una " Un empleado siempre es una persona, al revés no

class Persona:
    def __init__(self, nombre: str, edad: int, residencia: str):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def descripcion(self):
        print("Nombre:", self.nombre, "\nEdad:", self.edad, "\nResidencia:", self.residencia)


class Empleado(Persona):
    def __init__(self, salario: int, antiguedad: int, nombre: str, edad: int, residencia: str):
        super().__init__(nombre, edad, residencia)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):  # 1era Forma de hacerlo
        print("Nombre:", self.nombre, "\nEdad:", self.edad, "\nResidencia:", self.residencia, "\nSalario:",
              self.salario, "\nAntiguedad:", self.antiguedad)

    def descripcionn(self):  # 2da Forma de hacerlo
        super().descripcion()
        print("Salario:", self.salario, "\nAntiguedad:", self.antiguedad)


Antonio = Persona("Antonio", 55, "España")
Antonio.descripcion()

Manuel = Empleado(1500, 15, "Manuel", 55, "Colombia")
Manuel.descripcion()
Manuel.descripcionn()

print(isinstance(Manuel, Empleado))  # Comprobamos si Manuel pertenece a empleado, Manuel es de la clase empleado
print(isinstance(Manuel, Persona))  # Comprobamos si Manuel es persona, lo es

print(isinstance(Antonio, Persona))
print(isinstance(Antonio, Empleado))