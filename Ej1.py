#Ej1
"""
1.Creamos una variable para asociarla al bucle.
2.Creamos una variable que alamacenará las notas.
3.Cramos un bucle while.
4.Creamos una variable que almacena un input de notas.
4.1.Hacemos una condicion la cual si la variable anterior no es "exit" la nota debe ser un input y lo almacena en otra variable.
4.2.Hacemos una condicion la cual si la varaible anterior es "exit" la variable asociada al bucle cambie y se rompa el bucle.
4.3.Hacemos una condicion la cual si la variabile creada en el primer condicional no esta dentro de la variable notas, haga un append para añadirlo en la variable notas.
5.Creamos una variable que almacene la longitud de la lista "notas".
6.Creamos una variable que almacene la suma de la lista "notas".
7.Creamos una ultima variable que divida la variable que suma todas las notas entre la longitud de la lista de notas.
8.Por ultimo imprimimos por pantalla las notas, la media de las notas, la nota máxima sacada y la nota minima sacada.
"""
x = 1;
notas = [];

while x==1 :
    
    nota = input("Pon una nota:");
    
    if nota != "exit":
        respuesta = int(nota);
    
    if nota == "exit":
        x = 0;

    if respuesta not in notas:
        notas.append(respuesta)

i = len(notas);

suma = sum(notas);

media = suma/i;

print("Las notas fueron:", notas,"/", "La media es:",media,"/","La mayor nota fué:", max(notas), "/", "La menor nota fué:", min(notas));
