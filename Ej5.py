salida = 0
lista = []
num1 = int(input("Escribe un numero: " "\n"))
lista.append(num1)
print("Escribe un numero mayor que", num1)
num2 = int(input())

while salida == 0:
    if num1 < num2:
        lista.append(num2)
        num1 = num2
        print("Escribe un numero mayor a", num1)
        num2 = int(input())
    if num1 > num2:
        salida = 1
print("Los números que has escrito son:", lista)
