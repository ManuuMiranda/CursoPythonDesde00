# Listas:
milista = ["Mery", "Pepe", "Marta", "Antonio"]
# Orden de   0 a      1 a       2 a     3
print(milista)

print(milista[2])
print(milista[-1]) # Contando desde el final
print(milista[0:3]) # 3 primeros elementos, 0 incluido pero 3 no
print(milista[:3]) # Mismo resultado, obvia el 0
print(milista[1:2]) # Desde el índice 1 hasta el 2 sin incluir
print(milista[2:]) # 2 últimos elementos, desde el 2 hasta el final

## Agregar un término al final

milista.append("Sandra")

print(milista)

## Agregar un término en la posición que queramos

milista.insert(2,"Sandra")

print(milista)

## Agregar varios elementos a lista

milista.extend(["Sara", "Ana", "Lucía"])

print(milista)

print(milista.index("Antonio")) # Para saber el índice en el que se encuentra
print(milista.index("Sandra")) # Devuelve el primer elemento que se encuentra

print("Pepe" in milista) # Bool para ver si el elemento se encuentra en la lista

milista.remove("Ana") # Para eliminar elementos
print(milista)
milista.pop() # Elimina el útlimo elemento de una lista
print(milista)

milista2 = ["María",5,True,78.35] # Se puede hacer fácilmente

milista3 = ["Sandra", "Lucía"]

milista4 = milista2 + milista3 # Se pueden sumar listas

print(milista4)

milista5 = milista2 * 3 # Se repite la lista 3 veces

print(milista5)


# Tuplas:

