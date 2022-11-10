#Ej4

"""
Declaración de dos variables que alamacenan un input() cada uno recibir parámetros.
Utilizamos un condicional if para comparar los valores.
Si la respuesta 2 es mayor a la respuesta 1, se mostrará por pantalla que el segundo numero introducido es más grande.
En caso de que sea al reves usamos un else, se mostrará por pantalla que el  primer numero introducido es más grande.
"""

Resp1 = int(input("Escribe un num:"));
Resp2 = int(input("Escribe un num:"));

if Resp1 < Resp2:
    print(Resp2 , "Es mas grande");

else:
    print(Resp1 , "Es mas grande");
