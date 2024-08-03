#diccionarios
diccionario = {
    "nombre" : "balty",
    "apellido" : "martinez", #claves
    "subs" : 0

}
claves = diccionario.keys()
print(claves) #devuelve las claves

clave_2 = diccionario.get("nombre") #me encuentra la definicion
print(clave_2)

#clear elimina todos los elementos del diccionario
#diccionario.clear()


#con pop podemos eliminar un elemento cualquiera del diccionario
diccionario.pop("apellido")
print(diccionario)

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable) #me lo muestra por partes 

