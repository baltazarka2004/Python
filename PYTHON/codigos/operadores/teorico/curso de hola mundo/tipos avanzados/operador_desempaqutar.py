#lista1 = [1, 2, 3, 4]
#print(1, 2, 3, 4)
#print(*lista)

#lista2 = [5, 6]

#combinada = ["hola", *lista1, "mundo", *lista2] #el * es un operador de desempaquetamiento
#print(combinada)

punto1 = {"x": 19, "y": "hola"} #toma lso valores de derecha a izquierda
punto2 = {"y": 15, "z": "hola mundo"}

nuevopunto = { **punto1,"lala": "hola pitudos", **punto2} #esto une dos duiccionarios y los combino
print(nuevopunto)





    