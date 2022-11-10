"""
Almacenamos el ancho del triangulo en una variable pasada por parámetro.
Mediante un for recorremos el rango de la anterior variable + 1.
Mediante un segundo for recoremos un rango de la primera variable
Mediante un for anidado con el anterior recorremos un rango de 0 a la variable anterior menos el indice del segundo for.
"""

a = int(input("Escribe el ancho del triángulo: "))

for i in range(a+1):
    print("*" * i)

for i in range(a):
    for j in range(0,a - i):
        print("*", end="")
    
    print("")