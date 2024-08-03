def get_product(**datos): #para trabajar con los keyword arguments hay que poner un doble asterisco para que funcione
    print(datos["id"],datos["name"]) #con estop solo me imprimira el significado , por ejemplo id es 23 y name es iphone

get_product(id="23",
            name="iphone",
            edad="12") #en python cunado utilizo una funcion que continene las keyword arguments hay quwe SI O SI indicar el nombre del parametro y del argumento a la hora de llamar la funcion
#esto nos arroja un diccionario
# a la izquierda tenog el nombre del parametro y a la izqueierda el parametro
