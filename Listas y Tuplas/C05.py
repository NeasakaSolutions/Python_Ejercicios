# Escribir un programa que almacene en una lista los números del 1 al 10 
# y los muestre por pantalla en orden inverso separados por comas.

# Variables:
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Bucle de ordenamiento:
nueva_lista = sorted(lista_numeros, reverse = True)

# Impresion de la lista alreves:
for i in range(len(lista_numeros)):
        print(nueva_lista[i], end = ', ')

