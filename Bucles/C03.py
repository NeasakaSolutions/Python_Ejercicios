# Escribir un programa que pida al usuario un número entero positivo y 
# muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

# Variables:
num = int(input('Ingrese un numero entero: '))

# Ciclo para imprimir solo los numeros impares:

# La secuencia se compone en range(INICIO, FINAL, SALTO)
for i in range(1, num + 1, 2):
    print(i, end=', ')

