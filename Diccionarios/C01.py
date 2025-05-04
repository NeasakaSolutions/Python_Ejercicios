# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono 
# y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje 
# <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

# Variables:
datos_usuario = {
    'nombre' : '',
    'edad' : 0,
    'direccion' : '',
    'numero' : 0,
}

# Datos ingresados por el usuario:
datos_usuario['nombre'] = input('Ingrese su nombre: ')
datos_usuario['edad'] = int(input('Ingrese su edad: '))
datos_usuario['direccion'] = input('Ingrese su direccion: ')
datos_usuario['numero'] = int(input('Ingrese su numero: '))

# impresion de resultados:
print(f'{datos_usuario['nombre']} usted tiene {datos_usuario['edad']}',
      f' anios, vive en {datos_usuario['direccion']}',
      f'y su numero de telefono es {datos_usuario["numero"]}')
