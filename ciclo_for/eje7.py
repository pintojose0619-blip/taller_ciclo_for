"""
Caso. Se reciben los tiempos de N ciclistas, con 1 ≤ N ≤ 20, sobre una vuelta de 250 metros.
Cada registro contiene identificador entero positivo único, minutos enteros no negativos,
segundos entre 0 y 59 y centésimas entre 0 y 99. Cada tiempo total es positivo. Informe la
velocidad media de cada ciclista en kilómetros por hora y el identificador del ganador. En
empate de tiempo gana el primero recibido.
"""

n = int(input("ingrese numero de empleados "))

total_nomina = 0
mayor_sueldo = 0
menor_sueldo = 0
id_mayor = 0
id_menor = 0

for i in range(n):

    id_emp = int(input("ingrese identificador "))
    edad = int(input("ingrese edad "))
    antiguedad = int(input("ingrese años "))

    suma_ant = 0
    for j in range(antiguedad):
        suma_ant = suma_ant + (j + 1)


    sueldo = (100 + edad + suma_ant) / antiguedad
    total_nomina = total_nomina + sueldo


    if i == 0:
        mayor_sueldo = sueldo
        menor_sueldo = sueldo
        id_mayor = id_emp
        id_menor = id_emp
    else:
        if sueldo > mayor_sueldo:
            mayor_sueldo = sueldo
            id_mayor = id_emp
        if sueldo < menor_sueldo:
            menor_sueldo = sueldo
            id_menor = id_emp


    sueldo_cent = int((sueldo * 100) + 0.5)
    entero = sueldo_cent // 100
    decimales = sueldo_cent % 100


    if decimales < 10:
        print(id_emp, ": ", entero, ",0", decimales, ". ")
    else:
        print(id_emp, ": ", entero, ",", decimales, ". ")


nomina_cent = int((total_nomina * 100) + 0.5)
entero_n = nomina_cent // 100
decimales_n = nomina_cent % 100


if decimales_n < 10:
    print("Nómina: ", entero_n, ",0", decimales_n, ". ")
else:
    print("Nómina: ", entero_n, ",", decimales_n, ". ")

print("Mayor: ", id_mayor, ". Menor: ", id_menor )