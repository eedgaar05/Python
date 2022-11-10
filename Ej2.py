#Ej2

"""
Recoge 2 numeros en 2 variables.
Los dos numeros anteriores se convierten en un rango.
Mediante un for recorre ese rango y imprime cada numero en ese rango y indica si es par o impar.
"""
a = int(input("Dame un num: "));
b = int(input("Dame un num: "));
for i in range(a, b + 1):
    c = i % 2;
    if c == 0:
        print(i, "es par");
    if c != 0:
        print(i, "no es par");