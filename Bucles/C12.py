# Escribir un programa que muestre el eco de todo lo que el usuario introduzca 
# hasta que el usuario escriba “salir” que terminará.

# Variables:
boolean = True
eco_final = ''

# Bucle para el eco:
while boolean:
    eco = input('Ingrese un caracter: ')

    # Condicional para salir del bucle:
    if eco != 'Salir':
        eco_final += eco
    else: 
        boolean = False

print(eco_final) 
