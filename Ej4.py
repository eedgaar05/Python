salida = 0
lista = []

num1 = int(input("Escribe un numero: " "\n"))
lista.append(num1)
print("Escribe un numero mayor que", num1, ":")
num2 = int(input())

while salida == 0:

    if num2 > num1:
        lista.append(num2)
        salida = 1
    if num2 < num1:
        print(num2, "No es mayor que ", num1, " Introduce otro numero:")
        num2 = int(input())
print("Los números que has escrito son ", lista)