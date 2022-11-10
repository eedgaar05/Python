"""
Almacenamos 2 numeros en 2 varuiables.
Mediante un for recorremos un rango de 1 a la primera variable que define el numero de lineas.
Con un for anidado relizamos la misma acción con otro indice y la variable que define el numero de columnas.
"""

a = int(input("Escribe el numero de lineas: "));
b = int(input("Escribe el numero de columnas: "));

for i in range(1, a+1):
    for j in range(1, b+1):
        print("*", end="");
    print(" ");