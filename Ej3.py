#Ej3
"""
1.Declaramos una variable para que el usuario decida que area quiere calcular.
2.Declaramos un condicional que calcule el area de un tiangulo cuando el usuario escriba "triangulo" o "Tiangulo".
2.1.Dentro de este condicional declaramos 2 variables que corresponderan a la bas y la altura del triangulo.
2.2.Declaramos una variable la cual va a calcular el area del triangulo con la formula "(base * altura)/2".
2.3.Por ultimo antes de acabar el condicional imprimimos por pantalla la variable anterior para que nos muestre el area de los parametros que hemos introducido.
3.Declaramos otro condicional que calcule el area de un cuadrado cuando el usuario escriba "cuadrado" o "Cuadrado".
3.1.Dentro del condicional declaramos una variable con un imput() para definir la longitud de un lado del cuadrado
3.2.Declaramos una variable que nos calcule el area con la formula "lado * lado".
3.3.Por ultimo imprimimos por pantalla el resultado de la variable anterior.
4.Declaramos un else por si no introducen ni Cuadrado ni Triangulo.
"""
eleccion = input("Quieres calcular el area de un cuadrado o de un triangulo?");

if eleccion == "triangulo" or eleccion == "Triangulo":
    base = int(input("Escribe la base del triangulo:"));
    altura = int(input("Escribe la altura del triangulo."));

    areaTriangulo = (base * altura)/2;
    print("El resultado es", areaTriangulo);
    

if eleccion == "cuadrado" or eleccion == "Cuadrado":
    lado = int(input("Cuanto mide un lado del cuadrado?"));
    areaCuadrado = lado * lado;

    print("El resultado es", areaCuadrado);

else:
    print("No has introducido ninguna de las opciones.");
