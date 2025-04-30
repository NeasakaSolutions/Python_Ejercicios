# Escribir un programa que pida al usuario una palabra 
# y luego muestre por pantalla una a una las letras de la palabra introducida 
# empezando por la última.

# Variables:
palabra = 'Ijole'

# Bucle para separar los caracteres e imprimirlos de mayor a menor:
for i in range(len(palabra)):
    print(palabra[(-i -1)])
