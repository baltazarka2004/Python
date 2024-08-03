#pedirle un numero al usuario

numero = input("decime tu numero: ")

#multiplicamos con int
resultado = int(numero)*2

print(numero)

#ahora con float

resultado_f = float(numero)%2
resultado_final = float(numero)/2

if(resultado_f == 0 ):
    print("es par chabon")
else:
    print("no es par")
print(f"tu numero es {numero} y el resultado es {resultado_final}")