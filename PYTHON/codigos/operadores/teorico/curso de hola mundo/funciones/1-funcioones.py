def hola():#def para definior la funcion, dsp el nombre de la funcion y dos prentecis 
    print("hola como esta??")
    print("python")

def saludo(nombre): #aca con el parentecis le mando una variable que vamos a utilizar dentro de la funcion y solo la puedoutilizar dentro de la funcio, no fuera
    print(f"hola {nombre}")
                    
saludo("balty") #si o si hay que mandar el valor o nombre de la variable, ES OBLIGATORIO
saludo(input("nombre: ")) #aqui la variable pasa a ser un ARGUMENTO

def saludar (nombre, apellido): #aqui la variable le decimos PARAMETRO
    print (f"hola {nombre} {apellido}")
    
saludar("balty","martinez")

#podemos hacer que una funcion tenga un parametro por defecto si esq no queremops mandarlo como arguemnto, por ej 
def ejemplo (nombre , apellido="algo"):
    print(f"hola {nombre} {apellido}")
    
ejemplo("balty")#aca no mandamos un segundo argumente, entonces nos manda por defult "hola balty algo"



#puedo nombrar argumentos de la siguiente manera

saludar(apellido="martinez", nombre="balty")