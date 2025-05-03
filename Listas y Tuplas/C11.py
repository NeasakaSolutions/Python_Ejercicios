# Escribir un programa que almacene en una lista los siguientes precios, 
# 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

# Variables:
lista_precios = [50, 1, 75, 46, 22, 9, 80, 65, 8]
precio_alto = 0
precio_bajo = 0

# Recorrer toda la lista para los precios altos:
for i in range(len(lista_precios)):
    if lista_precios[i] > precio_alto:
        precio_alto = lista_precios[i]
    else:
        precio_bajo = lista_precios[i]

# Recorrer toda la lista para los precios bajos:
for x in range(len(lista_precios)):
    if lista_precios[x] < precio_bajo:
        precio_bajo = lista_precios[x]
    else:
        pass

print(f'El precio mas alto es de: {precio_alto}',
      f'y el precio mas bajo es de {precio_bajo}')
