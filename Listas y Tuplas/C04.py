# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

# Variables:
cantidad_de_numeros = 6
numeros = []

# Bucle para agregar los numeros:
for i in range(cantidad_de_numeros):
    numero = int(input(f'Ingrese el numero ganador {i + 1}: '))
    numeros.append(numero)

# Ordenamiento de la lista:
numeros.sort()

# Impresion de los numeros ganadores:
print(numeros)


