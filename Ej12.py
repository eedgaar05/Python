"""
1.Creamos una variable que almacena un input, el cual tiene que ser integer.
2.Creamos una variable indice que almacena un integer que usare posteriormente para un bucle.
3.Creamos una variable contador.
4.Creamos un bucle while que estara activo siempre que el indice no sea igual a la primera variable más uno.
4.1.Creamos una variable elección que divida con el operador % respuesta entre indice.
4.2.Aumentamos el indice +1.
4.3.Ponemos un condicional el cual si la variable elección es 0, la variable contador incrementa +1.
5.Creamos un condicional una vez acabado el bucle el cual si contador es igual a 2 imprima por pantalla que es primo.
6.Creamos otro condicional el cual si contador es mayor a 2 o menor a 2 imprima por pantalla que no es primo.
"""

respuesta = int(input("Escribe un numero: "));

indice = 1
cont = 0

while indice != respuesta + 1 :
    eleccion = respuesta % indice;
    indice += 1;
    if eleccion == 0:
        cont += 1;
if cont == 2:
    print(respuesta, "es primo.");
if cont < 2 or cont > 2:
    print(respuesta, "no es primo.")