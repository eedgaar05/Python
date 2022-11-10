#Ej2
"""
    1.Declaramos una variable del tipo array.
    2.Declaramos 5 variables con un imput() para pedir parámetros.
    3.Por cada variable con input posteriormente realizamos un append.
    3.1.El append es una funcion de python que nos permite añadir un elemento dentro de una lista.
    4.
    5.Mediante un condicional
"""
nums = []

num1 = int(input("Pon un num:"));
nums.append(num1);

num2 = int(input("Pon un num:"));
nums.append(num2);

num3 = int(input("Pon un num:"));
nums.append(num3);

num4 = int(input("Pon un num:"));
nums.append(num4);

num5 = int(input("Pon un num:"));
nums.append(num5);


if num1 < num2 and num2 < num3 and num3 < num4 and num4 < num5:
    print("La lista es creciente");

if num1 > num2 and num2 > num3 and num3 > num4 and num4 > num5:
    print("La lista es decreciente");
    

"""
else:
    print("La lista es desordenada");
    """