"""
Caso. Un vendedor tiene N ventas, con 0 ≤ N ≤ 1000, y se recibe el importe no negativo de cada
una. Informe cuántas fueron de 200 o menos, cuántas superaron 200 sin llegar a 400 y cuántas
fueron de 400 o más. Una venta pertenece a un solo grupo.
"""

numero_ventas = int(input("Ingrese numero de ventas "))

if  0 <= numero_ventas <= 1000:
    grupo1 = 0
    grupo2 = 0
    grupo3 = 0
    for k in range(numero_ventas):
        
        ventas = int(input(" ingrese el valor de la venta "))

        if ventas <= 200:
            grupo1  = grupo1 + 1

        elif 200 < ventas < 400:
            grupo2 = grupo2 + 1

        else:
            grupo3 = grupo3 + 1

    print("gupos 1, 2 y 3: ",grupo1 , grupo2, grupo3 )
else:
   print("no cumplen con los parametros")