punto = { "x": 25, "y": 50}  #solamente acepta los strings, definimos con un string y el valor dsp de los 2 putos
print(punto)
print(punto["x"]) #para acceder debo de poner el nombre que le defini


punto ["z"] = 55 #aqui creamos una nueva llave dentro de ldiccionario
print(punto)

if "lala" in punto:
    print("encontre a lala ", punto["lala"])
    
#para acceder
print(punto.get("x"))
print(punto.get("lala")) #nos devulve none si esq no hay nada dentro del diccionario
#lo que tmb podemos hacer es definir un valor por defecto cuadno algo no se encuentre dentro del dicciionario
print(punto.get("lala", 97)) 
del punto["x"]
del (punto["y"])
print(punto)
punto["x"] = 25
#una forma de acceder
for valor in punto:
    print(valor, punto[valor])
#otra foram para acceder

for valor in punto.items():
    print(valor) #nos esta devolviendo tuplas

for llave, valor in punto.items():
    print(llave, valor) 
    


usuarios = [
    {"id": 1, "nombre": "chancho"},
    {"id": 2, "nombre": "nico"},
    {"id": 3, "nombre": "balty"},
    {"id": 4, "nombre": "jorge"},



]

for usuario in usuarios:
    print(usuario["nombre"])
    
    