#cuando no sabemos cauntos argumentos le vamos a mandar a la funcion haremos lo siguiente:
def suma(*numeros):#le vamos a poner un asterisco al principio del parametro
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)
        
        
    
suma(2,5,7)
suma(1,3,5,76,2,1) #esto va a ser iterable