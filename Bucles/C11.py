# Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase.

# Variables:
frase = input('Ingrese una frase: ')
letra = input('Ingrese una letra: ')
contador_letra = 0

# Bucle para recorrer la frase
for i in range(len(frase)):

    # COndicional para aumentar el contador:
    if frase[i] == letra:
        contador_letra += 1
    else:
        pass

# Impresion del contador:
print(contador_letra)


