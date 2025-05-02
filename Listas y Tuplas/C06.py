# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
# pregunte al usuario la nota que ha sacado en cada asignatura 
# y elimine de la lista las asignaturas aprobadas. 
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

# Variables:
lista_asignaturas = ['Matematicas', 
                     'Fisica', 
                     'Quimica', 
                     'Historia',
                     'Lengua']

lista_reprobadas = []

# Recorrer la lista asignatura para obtener la calificacion:
for i in range(len(lista_asignaturas)):
    # Obtener calificaciones de forma individual:
    calificaciones = float(input(f'Ingrese la calificacion de la materia {lista_asignaturas[i]}: '))

    # Separar calificaciones aprobatorias
    if calificaciones < 6:
        lista_reprobadas += [lista_asignaturas[i]]
    else:
        pass

# Impresion de la lista de asignaturas no aprobadas:
print(lista_reprobadas)


