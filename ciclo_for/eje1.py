"""
EJERCICIO 1
Secuencia entre dos límites

Caso. Una pantalla debe presentar todos los enteros comprendidos entre dos límites A y B,
ambos incluidos, empezando por A y terminando en B. Los límites son enteros entre -100 y
100. Si coinciden, presente ese único valor.

Fórmula o relación: El paso entre términos es 1 si A ≤ B y -1 si A > B.
"""

a = int(input("ingrese limite "))
b = int(input("ingrese limite "))

if a <= b and (100 > a and 100 > b ) and (-100 < a and -100 < b):
    print(list(range(a, b+1)))
elif a > b and (100 > a and 100 > b ) and (-100 < a and -100 < b):
    print(list(range(a, b-1)))
else :
    print("Los valores dijitados no estan entre el rango permitido -100 , 100")
