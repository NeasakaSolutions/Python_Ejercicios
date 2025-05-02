# Escribir un programa que almacene el abecedario en una lista, 
# elimine de la lista las letras que ocupen posiciones múltiplos de 3, 
# y muestre por pantalla la lista resultante.

# Variables:
abecedario = list("abcdefghijklmnopqrstuvwxyz")
abecedario_nuevo = []

# Recorrer la lista
for i in range(len(abecedario)):
    if (i % 3) != 0:
        abecedario_nuevo.append(abecedario[i])
    else:
        pass

# Impresion del nuevo abecedario
print(abecedario_nuevo)



