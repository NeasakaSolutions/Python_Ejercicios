# Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

# Variables:
inversion_inicial = float(input('Ingrese su inversion inicial: '))
interes = int(input('Ingrese el interes sin el signo "%": '))
anios = int(input('Ingrese el numero de anios de inversion: '))
transformar_decimal = interes / 100

# Iterar la capital:
for i in range(anios + 1):
    nueva_capital = (inversion_inicial * (1 + transformar_decimal) ** i)

    # Impresion apartir del anio 1:
    if i == 0:
        pass
    else:
        print(f'El anio {i} tuvo una capital de: {round(nueva_capital, 2)}')
