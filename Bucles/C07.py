# Escribir un programa que pida al usuario un número entero 
# y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
# *
# **
# ***
# ****
# *****

# Variables:
num = int(input('Ingrese un numero entero: '))

# Ciclo de iteracion:
for i in range(num + 1):
    print('*' * (i))

