# Escribir un programa que pida al usuario una palabra 
# y muestre por pantalla el número de veces que contiene cada vocal.

# Variables:
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0 
vocales = []
palabra = input('Ingrese una palabra:').lower()

# Recorrer la palbra:
for i in range(len(palabra)):
    if 'a' == palabra[i]:
        contador_a += 1
    elif 'e' == palabra[i]:
        contador_e += 1
    elif 'i' == palabra[i]:
        contador_i += 1
    elif 'o' == palabra[i]:
        contador_o += 1
    elif 'u' == palabra[i]:
        contador_u += 1

# Agregar a la lista:
vocales.append(contador_a)
vocales.append(contador_e)
vocales.append(contador_i)
vocales.append(contador_o)
vocales.append(contador_u)

print(f'La vocal "a"  se repite: {vocales[0]} veces.',
      f'\nLa vocal "e" se repite: {vocales[1]} veces.',
      f'\nLa vocal "i" se repite: {vocales[2]} veces.',
      f'\nLa vocal "o" se reipte: {vocales[3]} veces.',
      f'\nLa vocal "u" se repite: {vocales[4]} veces.')


