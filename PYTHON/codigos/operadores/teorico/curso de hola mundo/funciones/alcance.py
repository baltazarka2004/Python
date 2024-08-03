saludo = "hoooola"

def saludar (): #solo voy a poder acceder a las variables "saludo" dentro de la misma funcion ya que ese es su alcance
    saludo = "hola balty"
    print(saludo) #nos va a tirar error pq la variable local nno se le asigno un valor
    
def saludoperso ():
    global saludo #mala practica
    saludo = "hola persona"#son dos variables completamente distintas , ya que se uardan en distintos lugare de la pc
    
print (saludo)
saludar()
print(saludo)