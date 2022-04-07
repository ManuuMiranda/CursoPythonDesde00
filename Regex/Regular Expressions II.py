import re

lista_ciudades = ['Ma1',
                  'Se1',
                  'Ma2',
                  'Ba1',
                  'Ma3',
                  'Va1',
                  'Va2',
                  'Ma4',
                  'MaA',
                  'Ma5',
                  'MaB',
                  'MaC']

for elemento in lista_ciudades:
    if re.findall('Ma[0-3]', elemento):
        print(elemento)

for elemento in lista_ciudades:
    if re.findall('Ma[^0-3]', elemento):  # Aquí utilizamos el ^ para hacer la negación del rango
        print(elemento)

for elemento in lista_ciudades:
    if re.findall('Ma[0-3A-B]', elemento):  # Cuando los códigos son letras y números
        print(elemento)


# Ejemplo con anotaciones diferentes:
print("Ejemplo con anotaciones diferentes:")

import re

lista_ciudades2 = ['Ma.1',
                  'Se1',
                  'Ma2',
                  'Ba1',
                  'Ma:3',
                  'Va1',
                  'Va2',
                  'Ma4',
                  'MaA',
                  'Ma.5',
                  'MaB',
                  'Ma:C']

for element in lista_ciudades2:
    if re.findall('Ma[.:]', element):
        print(element)