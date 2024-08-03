#saludemos al usuario
def hola(nombre):
    return "hola "+ nombre+ "!" 
def saludar():
    nombre = input("ingresar nombre porfavr: ")
    saludo = hola(nombre) 
    print(saludo)
saludar()