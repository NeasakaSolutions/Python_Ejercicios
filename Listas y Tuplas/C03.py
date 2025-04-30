# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
# pregunte al usuario la nota que ha sacado en cada asignatura, 
# y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> 
# donde <asignatura> es cada una des las asignaturas de la lista 
# y <nota> cada una de las correspondientes notas introducidas por el usuario.

# Vaiables:
asignaturas = ['Matematicas', 
               'Fisica', 
               'Qimica', 
               'Historia', 
               'Lengua']

calificaciones = []

# Bucle para recorrer la lista:
for i in range(len(asignaturas)):
    nota = float(input(f'Ingrese la nota de {asignaturas[i]}: '))
    calificaciones.append(nota)

# Bucle recorrer ambas listas:
for i in range(len(asignaturas)):
    print(f'En {asignaturas[i]} tu nota es: {calificaciones[i]}.')
