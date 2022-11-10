#Ej5
"""
1.Declaramos una variable con un imput().
2.Declaramos 7 variables para dividir el importe entre cada uno de los billetes existentes.
2.1.Lo dividimos con el operador "%" para que sepamos si el importe es divisible entre el valor de los billetes.
3.Posteriormente declaramos otras 7 variables para dividir el importe.
3.1.Lo dividimos con el operador "/" para saber la cantidad exacta de billetes de dicho valor se necesitan para llegar al importe.
4.Realizamos 7 concicionales para comprobar si el resultado de las divisiones con "%" es 0.
4.1.En caso de que sea 0 nos imprimirá por pantalla el importe y la cantidad de billetes x que se necesitan para llegar a la cantoidad del importe. 
"""

importe = int(input("Introduce el dinero que quieres retirar:"));

vuelta1 = importe % 5;
division1 = importe / 5;

vuelta2 = importe % 10;
division2 = importe / 10;

vuelta3 = importe % 20;
division3 = importe / 20;

vuelta4 = importe % 50;
division4 = importe / 50;

vuelta5 = importe % 100;
division5 = importe / 100;

vuelta6 = importe % 200;
division6 = importe / 200;

vuelta7 = importe % 500;
division7 = importe / 500;

if vuelta1 == 0:
    print("Tu importe es de", importe, ", el cajero te devuelve", division1, "billetes de 5€");

if vuelta2 == 0:
    print("Tu importe es de", importe, ", el cajero te devuelve", division2, "billetes de 10€");

if vuelta3 == 0:
    print("Tu importe es de", importe, ", el cajero te devuelve", division3, "billetes de 20€");

if vuelta4 == 0:
    print("Tu importe es de", importe, ", el cajero te devuelve", division4, "billetes de 50€");

if vuelta5 == 0:
    print("Tu importe es de", importe, ", el cajero te devuelve", division5, "billetes de 100€");

if vuelta6 == 0:
    print("Tu importe es de", importe, ", el cajero te devuelve", division6, "billetes de 200€");

if vuelta7 == 0:
    print("Tu importe es de", importe, ", el cajero te devuelve", division7, "billetes de 500€");