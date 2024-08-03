# las tuplas es casi lo simo que las listas, 
# lo que difiere de las 
# listas esq las tuplas no se pueden modificar


numeros =(1, 2, 3,4) + (4, 5, 6) 
# los parentecis demuestran que no queremos modificar los elemntos dentro de las tuplas

print(numeros)

punto = tuple([1, 2]) #recibe cualqueir dato que sea iterable
print(punto)

menosnumero = numeros[:2]
print(menosnumero)

primero, segundo, *otros = numeros
print(primero, segundo, otros)

for n in numeros:
    print(n)

#numeros [0] = 5 no se puede hacer esto

# si esto:

listanumeros = list(numeros)
listanumeros[0] = "chanco"
print(listanumeros)