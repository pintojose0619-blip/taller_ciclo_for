"""
Caso. Una inversión ficticia inicia con capital C no negativo y mantiene una tasa anual
porcentual I con 0 < I < 100. Se recibe también un entero M entre 0 y 50. El interés de cada año

es el saldo al comienzo de ese año multiplicado por I y dividido entre 100; se suma al saldo al
final del año. Determine el saldo después de M años; con M = 0 conserva el capital inicial.
"""

c = int(input("Ingrese capital "))
i = int(input("Ingrese tasa anual "))
m = int(input("Ingrese interes anual "))


if (c >= 0) and (0 < i < 100) and (m > 0 and m < 50) :
    saldo = c
    for k in range(m):
        saldo = saldo * (1 + i /100)

    print(saldo)
else:
   print("ff")