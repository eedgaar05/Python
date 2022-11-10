
"""
Almacenamos un numero pasado por pantalla.
Comprobamos que el numero no sea 0 o menor que cero.
(Ya que si es negativo no existe su factorial y si es 0 su factorial es 1)
Mediante un bucle while calculamos el factorial y le vamos restando 1 a la primera variable.
"""

num = int(input("Escribe un numero para calcular el factorial: "));

if num < 0:
    print("El factorial de un numero negativo no existe")
if num == 0:
    print(1)

factorial = 1
while num > 0:
    factorial = factorial * num
    num -= 1
print("El factorial de", num, "es", factorial)