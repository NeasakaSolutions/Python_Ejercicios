# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

# Variables:
password = 'ijole'
password_user = input('Ingrese la password: ')

# Verificar que la password sea correcta:
if password.lower() == password_user.lower():
    print('Correct password')
else:
    print('Incorrect password')


