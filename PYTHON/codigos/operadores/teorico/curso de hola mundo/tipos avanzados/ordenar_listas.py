numeros = [5, 3, 6, 90 ,2 , 4, 1, 5]
#numeros.sort(reverse=True) #con sort ordeno los numeros, 
numeros2 = sorted(numeros, reverse=True) #sorted devulve una nueva lista, no nos devulve la anterior
print(numeros2)
print (numeros)

usuarios = [
    [4, "chancho"], 
    [5, "balty"],
    [1, "felipe"]]

usuarios.sort()
print(usuarios) #esto me lo ordena ya que le estoy pasando un id al principio pero si se lo paso dssp del nombre pasaria lo siguietne:

usuarios2 = [
    ["chancho", 2], 
    ["balty", 4],
    ["felipe", 1]]


def ordena (elemento):
    return elemento[1] #esta funcion lo que hace es  que le retorna el segundo elemento del listado, ose aen este cas o seria el "2"

usuarios2.sort(key=lambda el: el[1]) 
#utilizo estas funcones "fantasmas" o lambda cuando una funcion la voy a utilizar solo 1 vez en todo el programa 
#el paramentor que le eestoy mandando es ele elemento y el valor de retorno es ele "return eleemnto" 
#usuarios2.sort(key=lambda parametro:valorRetorno)
print(usuarios2) 