#crenado una lista con list

lista = list(["hola", "balty",34, "yyyy mia voo","puto"])
#si usamos len (funcion) pasa esto
resultado = len(lista)

print(resultado) # me devuelve la cantidad de elementos dentro de la lista

#agregando elementos a la lista

agregando_con_append = lista.append("JA me cole")


#agregando un elemento a la lista en un indice

lista.insert(1,"no soy")
print(lista)

#agregando varios elemento a la lista 

lista.extend(["fatal", 2029])
print(lista)

#borrando elementos de la lista por su indice

lista.pop(-1)#con el "-" se elemina desde atras cuando es negativo
lista.pop(0)#elimina elemento con indice desde delante
print(lista)
#remociendo un elemento por su valor
lista.remove("no soy")
print(lista)

#list.clear()
#ordena la lista
lista2 = list([234,123,1251,567,False])
lista2.sort() 
print(lista2)
lista2.sort(reverse=True) #no funciona con cadenas de texto
print(lista2)

#invirtiendo la lista 
lista2.reverse()
print(lista2)
