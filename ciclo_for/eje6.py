"""
Caso. Se reciben los tiempos de N ciclistas, con 1 ≤ N ≤ 20, sobre una vuelta de 250 metros.
Cada registro contiene identificador entero positivo único, minutos enteros no negativos,
segundos entre 0 y 59 y centésimas entre 0 y 99. Cada tiempo total es positivo. Informe la
velocidad media de cada ciclista en kilómetros por hora y el identificador del ganador. En
empate de tiempo gana el primero recibido.
"""


n = int(input("ingresar numero de ciclistas"))

mejor_tiempo = 0
ganador = 0

for i in range(n):
    id_ciclista = int(input("ingresa id"))
    minutos = int(input("ingresa minutos"))
    segundos = int(input("ingresa segundos"))
    centesimas = int(input("ingresa centesimas"))


    tiempo = 60 * minutos + segundos + centesimas / 100
    velocidad = 900 / tiempo


    if i == 0:
        mejor_tiempo = tiempo
        ganador = id_ciclista
    elif tiempo < mejor_tiempo:
        mejor_tiempo = tiempo
        ganador = id_ciclista


    entero = int(velocidad)
    decimales = int((velocidad - entero) * 100)

    if decimales == 0:
        print(id_ciclista, ": ", entero, ",00 km/h. ")
    elif decimales < 10:
        print(id_ciclista, ": ", entero, ",0", decimales, " km/h. ")
    else:
        print(id_ciclista, ": ", entero, ",", decimales, " km/h. ")

print("Ganador: ", ganador)
