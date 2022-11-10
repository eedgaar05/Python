"""
Almacenamos el ancho del triangulo en una variable.
Mediante un for recorremos un rango de la anterior variable + 1
Imprimimos * multiplicado por el indice del for anterior.
"""

a = int(input("Escribe el ancho del triángulo: "))

for i in range(a+1):
    print("*" * i)