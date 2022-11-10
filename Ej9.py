"""
Almacenamos la anchura y la altura en dos variables diferentes.
Mediante un for recorremos el rango de la primera variable.
Con un segundo for con un rango de la segunda variable - 2.
Con un for anidado recorremos el rango de la primera variable - 2.
Con un tercer for vuelvo a recorrer el rango d ela primera variable.
"""

a = int(input("Anchura del rectángulo: "))
b = int(input("Altura del rectángulo: "))

for i in range(a):
    print("* ", end="")
print()

for i in range(b - 2):
    print("* ", end="")
    for j in range(a - 2):
        print("  ", end="")
    print("*")

for i in range(a):
    print("* ", end="")