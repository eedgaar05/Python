salida = 0
lista = []
while salida == 0:
    palabra = input("Escribe una palabra: ")
    if palabra != "":
        lista.append(palabra);
    if palabra == "":
        salida = 1
print("Las palabras que has Escrito son" , lista);
