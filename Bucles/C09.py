# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

# Variables:
password = 'Contrasena'
boolean = True

# Ciclo:
while boolean:
    password_user = input('Insert password: ')

    # Condicional para repetir bucle while
    if password == password_user:
        print('Correct password')
        boolean = False
    else:
        print('Incorrect password')

