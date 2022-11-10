#Ej3

"""
Recoge 2 números en 2 variables.
Una tercera variable almacena el rango entre los dos numeros anteriores.
Mediante un for en una variable vacia le sumamos los indices.
"""

a = int(input("Escribe un num: "));
b = int(input("Escribe un num mayor al anterior:"));
c = range(a, b+1);

suma = 0
for i in c:
    suma +=i

print(suma)