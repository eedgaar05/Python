salida = 0
lista = []
while salida == 0:
    numero = input("Escribe un numero: ")

    if numero != "Salir":
        num = int(numero)
        lista.append(num)

    if numero == "Salir":
        salida = 1
print("Los números que has escrito son ",lista)