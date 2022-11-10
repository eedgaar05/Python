"""
Almacenamos la altura del triangulo en una variable.
Mediante un for recorremos un rango de 1 a la primera variable + 1.
Con un for anidado recorremos un rango de la primera variable - el indice del primer for.
Con otro for anidado en el primero recorremos un rango de 1 a 2 * el primer indice.
"""

a = int(input("Altura del triangulo: "))

for i in range(1, a + 1):
    for j in range(a-i):
        print(" ", end="")
    for j in range(1, 2 * i):
        print("*", end="")
    print()