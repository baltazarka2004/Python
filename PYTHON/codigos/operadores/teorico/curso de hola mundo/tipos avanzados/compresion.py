usuarios2 = [
    ["chancho", 3], 
    ["balty", 4],
    ["felipe", 1]]

#imaginemos quesolo queremos una lista de usuario o de nombre, queremos transformar esta lista:
#forma fea
#nombre = []
#for usuario in usuarios2:
 #   nombre.append(usuario[0])
#print(nombre)

#forma linda:
#nombre = [expresion (escribimos la exprecion con el elemento que queremos que nos retone) for item ( como lo vamos a llamar) in items(que estamos iterando)]


#esot se conoce como MAP
#nombre = [usuario[0] for usuario in usuarios2] esto es trsnformacion


#y esto se conoce como FILTER

#ahora vamos a filtrarlo
#nombres = [expresion for items in items]
#nombres = [usuario for usuario in usuarios2 if usuario[1] > 2] # esto es fuiltarado
#poodemos convinar ambas cosas 

#nombres = [usuario[0] for usuario in usuarios2 if usuario[1] > 2]

#MAP
#nombres = list(map(lambda usuario: usuario[0], usuarios2))

#FILTER
menosusuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios2)) #si evalua en true devuelve el elemento y si evalua en flase no devuleve nada



print(menosusuarios)



