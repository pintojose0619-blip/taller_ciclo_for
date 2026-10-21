"""
Caso. Una empresa tiene N empleados, con 0 ≤ N ≤ 1000. Se recibe el sueldo no negativo de
cada empleado y se desea el total de la nómina. Para una empresa sin empleados, el total es
cero.
"""

n_empleados = int(input("Ingrese numero de empleados "))


if 0 <= n_empleados <= 1000:
    nomina = 0
    for k in range(n_empleados):
        salario = int(input("ingrese salario ") )
        nomina = nomina + salario    
    print("La nomina es ", nomina )
else:
    print("Valores inválidos (es negativo)")