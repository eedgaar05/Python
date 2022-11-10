#Ej3
"""
1.Declaración de una variable que alamacena un input() para recibir parámetros.
2.Declaramos una segunda variable que divida la primera entre 2 utilizando "%"
2.1.Cuando se utiliza el simbolo "%" lo que hace es que se dividan dos numeros y como respuesta te mueste el residuo de la división.
3.Por ultimo realizamos un if y un else para que conpruebe si el resultado de la variable anterior es 0.
3.1.En caso de que sea 0 el numero introducido en la primera variable es par.
3.2.En caso de que no sea 0 el numero introducido en la primera variable no es par.
"""

N = int(input("Escribe un num:"));
division = N % 2;
if division == 0:
    print(N , "Es par");
else:
    print(N , "No es par");