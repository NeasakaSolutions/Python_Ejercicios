# Escribir un programa que pida al usuario un número entero y 
# muestre por pantalla un triángulo rectángulo como el de más abajo.
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

# Variables:
#num = int(input('Igrese un numero entero: '))
num = 9

# Ciclo para numeros impares:
'''
for x in range(1, contador + 1, 2):
    print(x, end=',')
'''

# Ciclo para la estructura del triangulo
for x in range(1, num + 1, 2):
    for y in range(x, 0, -2):
        print(y, end=' ')
    print(' ')