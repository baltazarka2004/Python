#calcular el factorial de un numero
numero = int(input("ingresar numero para hacer su factorial: "))
def factorial():
    fac = 1
    for x in range (1,numero+1):
        fac = x*fac
    return fac

fac = factorial()
print(fac)