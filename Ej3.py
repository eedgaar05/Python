salida = 0
lista = []
while salida == 0:
    nota = float(input("Escribe una nota: "))
    
    rango = range(0, 11)

    if nota in rango:
        lista.append(nota)
    else:
        salida = 1
print("Las notas que has Escrito son",lista);