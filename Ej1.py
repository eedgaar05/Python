#Ej1
""" 1.Declaramos una variable del tipo array.
    2.A contuniación declaramos 5 variables con input() para pedir parámetros.
    3.Por cada variable con input posteriormente realizamos un append.
    3.1.El append es una funcion de python que nos permite añadir un elemento dentro de una lista.
    4.Definimos dos variables con las funciones min() y max().
    4.1.La funcion min() nos extrae el valor más pequeño dentro de una lista.
    4.2.La funcion max() nos extrae el valor más grande dentro de una lsita.
    5.Imprime por pantalla los valores almacenados en las variables anteriores.
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

minimo = min(nums);
maximo = max(nums);

print(
    minimo, "es el numero más pequeño." "\n",
    maximo, "es el numero más grande.");
