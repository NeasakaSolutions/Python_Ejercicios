# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas 
# y muestre por pantalla su producto escalar.

# Variables:
vector_1 = [1, 2, 3]
vector_2 = [-1, 0, 2]
productos_vectores = []
producto_escalar = 0

# Recorrer las listas:
for i in range(len(vector_1)):
    productos_vectores.append(vector_1[i] * vector_2[i])
    producto_escalar += productos_vectores[i]

# Impresion del resultado:
print(f'El producto escalar de ambos vectores es: {producto_escalar}')
