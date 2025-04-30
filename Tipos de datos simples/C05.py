# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde.

# Variables:
hrs_trabajadas = int(input('Ingrese las horas trabajadas: '))
coste_hora = int(input('Ingrese el coste por hora: '))

# Operaciones
resultado = hrs_trabajadas * coste_hora

# Impresion de resultados
print(f'La paga correspondiente es de: {resultado} eur.')


