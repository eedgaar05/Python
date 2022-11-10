salida1 = 0
salida2 = 0
lista = []

num1 = int(input("Escribe un numero: " "\n"))

print("Escribe un numero mayor", num1)
num2 = int(input())

while salida1 == 0:
    if num1 < num2:
        salida1 = 1
        rango = range(num1, num2)
    if num1 > num2:
        print(num2, "no es mayor a", num1, ".Vuelve a probar:")
        num2 = int(input())

while salida2 == 0:
    print("Escribe un numero entre", num1, "y",num2)
    num3 = int(input())

    if num3 in rango:
        lista.append(num3)
    
    else:
        salida2 = 1

lst_str = str(lista)[1:-1]
print("Los números situados entre", num1, "y", num2, "que has escrito son:", lst_str)