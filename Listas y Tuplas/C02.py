# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista 
# y la muestre por pantalla el mensaje Yo estudio <asignatura>, 
# donde <asignatura> es cada una de las asignaturas de la lista.

# Variables:
asignaturas = ['Matematicas', 
               'Fisica', 
               'Qimica', 
               'Historia', 
               'Lengua']

# Bucle para recorrer la lista:
for i in range(len(asignaturas)):
    print(f'Yo estudio: {asignaturas[i]}')

