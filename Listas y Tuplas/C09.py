# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

# Variables:
palabra = input('Ingrese una palabra: ')

# Invertir la palabra:
palabra_invertida = palabra[::-1]

# Verificar si es un palindromo
if palabra.lower() == palabra_invertida.lower():
    print(f'La palabra "{palabra}" es un palindromo. ')
else:
    print(f'La palabra "{palabra}" no es un palindromo. ')

