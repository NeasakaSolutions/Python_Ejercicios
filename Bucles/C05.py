# Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

# Variables:
num = int(input('Ingrese un numero entero: '))

# Ciclo para la impresion de la secuencia:
for i in range(num + 1):
    print(num - i, end=', ')

