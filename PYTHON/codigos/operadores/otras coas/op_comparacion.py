cadena1=("ESTABA EN MAYUSCULA YO")
cadena2= ("hola soy balty")
cadena3=("wtf")
final= cadena1.lower()
#buscar en una cadena otra cadena, te devuelce -1 si no hay nada 
print(final.find("m"))
##buscar en una cadena otra cadena, te lanza una exepcion
print(final.index("a"))


#si en numero o no 
print("59012".isnumeric())

#si es un alphanumerico (de la A a la Z) los caracteres especiales como los espacios, "-", "_", entre otros no cuenta


print("soyalpha".isalpha())

#contamos coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias
print(final.count("a"))
#contamos cuantos caracteres tiene una cadena (funcion)
print(len(final))

#verificamos si una cadena empieza con otra dada

print(final.startswith("estaba"))

#verificamos si una cadena termina con otra dada

print(cadena2.endswith("balty"))

#remplaa un pedazo de la cadena dada por otra

remplazo = cadena2.replace("ty","to")
remplazo = remplazo.upper()

print(remplazo)

#separar cadenas con las cadena que le pasemos 
cadena_separada = cadena1.split(" ") #separa por espacios
print(cadena_separada[3])