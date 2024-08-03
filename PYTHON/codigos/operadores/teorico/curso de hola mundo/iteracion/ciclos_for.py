#ciclo for: 
for numero in range(5):
    print(numero)
    
    
#ciclo for else 
buscar = 10
for numero in range(5):
    if numero == buscar:
        print(numero)
        break #detiene la ejecucion del codigo
else:
    print("no se encontro el numero deseado")#utilizo el else por si no se utilizo o no se toco nunca la parte de lcodigo llamada "break"
    
    
#tipos de iterables ( se ve mas adealnte): string, tuplas, lista
for char in "ultimate spiderman":
    print(char)#imprime letra por letra
    