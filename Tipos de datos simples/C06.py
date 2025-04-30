# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase 
# Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

# Variables:
peso = float(input('Ingrese su peso en kg: '))
altura = float(input('Ingrese su altura en mts: '))

# Operaciones
imc = (peso / (altura ** 2))
imc_final = round(imc, 2) # Redondeado a dos decimales

# IMpresion de resultados:
print(f'Tu IMC es de: {imc_final}')

