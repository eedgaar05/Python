#Ej4
"""
1.Declaramos 4 variables con imput().
2.Declaramos otras tres variables que dividan las tres primeras variables anteriores entre la ultima variable con el simbolo "%".
2.1.Cuando se utiliza el simbolo "%" lo que hace es que se dividan dos numeros y como respuesta te mueste el residuo de la división.
3.Declaramos tres condicionales anidados que cuando el residuo de las tres variables anteriores sea 0 diga si son divisibles o no.
"""
num1 = int(input("Pon un num:"));
num2 = int(input("Pon un num:"));
num3 = int(input("Pon un num:"));
num4 = int(input("Pon un num:"));

operacion1 = num1 % num4;
operacion2 = num2 % num4;
operacion3 = num3 % num4;

if operacion1 == 0:
    if operacion2 == 0:
        if operacion3 == 0:
            print(num4, "es divisible entre", num1, num2, num3);
        else:
            print(num4, "no es divisible entre", num1, num2, num3);
