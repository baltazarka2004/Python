numero = [1, 2,3]
#esto esta medio mal visto:
#primero = numero[0]
#segundo = numero [1]
#tercero = numero [2]

primero, segundo, tercero = numero #esto desempaqueta el listado de la lista
print(primero)


#si quiero obtener un solo elemento de la listo hago lo siguiente

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]


prim, segundos, terceros, *otros, ultimo = numeros #con el asterico lo que hago es meter el resto de elementos en la variable "otros"
print(prim,segundos,terceros,ultimo,otros)


