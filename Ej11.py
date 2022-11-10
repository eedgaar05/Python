"""
Almacenamos un numero en una variable pasado por parámetros.
Mediante un for recorremos un rango de 1 a la priemra variable + 1.
Dentro del for realizamos un condicional para poder añadir el indice a una lista si cumple dicha condicion.
"""

num = int(input("Escribe un numero: "))
lista = []

for i in range(1,num +1):
    division = num % i
    if division == 0:
        lista.append(i)
print(lista)