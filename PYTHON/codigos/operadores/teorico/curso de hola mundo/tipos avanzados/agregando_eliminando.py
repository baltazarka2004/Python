mascotas = [
    "perro",
    "gatos",
    "perro",
    "rata", 
    "gatos",
    "vaca"
 ]

mascotas.insert(1, "melvin") #para agregar algo al listado lo que hago es : uso insert(indice, valor/nombre/etc)
mascotas.append("chacho triste")# para agregar un elemento al final de la lista

#y para eliminar elementos dentro de un listado

mascotas.remove("perro") #remueve solo la primera, para eleminar todas los elementos que aparecen con ese nombre, deberiamos priemro contar y ponerlo la cantidad de veces que aparece
mascotas.pop(0)#para eliminar el ultimo elemento de una lista no le pongo un indice dentro del parentecis, si quieroeliminar un elemento en especifico lo pongo
#melcin en este caso esw el elemento 0
del mascotas[0]
#para limpiar el arreglo completo hago:
mascotas.clear()


print(mascotas)