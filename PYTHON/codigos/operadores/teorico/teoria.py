
 #cuadrado de un numero dado
def cuadrado(num):
    return num*num
    
print(cuadrado(2))



#Piensa un número, duplícalo, súmale 6, divídelo por 2 y resta el número que
#elegiste al comienzo. El número que queda es siempre 3.


def numero_ram(numero):
   return  ((((numero*2)+6)/2)-numero)
    
print(numero_ram(10))





#suamr el cuadrado de los 5 primeros numeros

def suma_cuadrado(n):
    suma=0
    for x in range (1,n+1):
        suma = suma + cuadrado(x)
    return suma

print(suma_cuadrado(5))


help("for")


