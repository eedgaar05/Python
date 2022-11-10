suma  = 0
lista = []
limite = int(input("Escribe un numero que actuará como limite: "))

while suma < limite:
    num = int(input("Escribe un número que se ira sumando: "))
    lista.append(num)
    suma = suma + num

lst_str = str(lista)[1:-1]
print("El limite que debe alcanzar es", limite, ".La lista creada es", lst_str, "ya que la suma es", suma)
