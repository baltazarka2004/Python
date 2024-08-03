frase= input("decime una frase para calcular cuanto tenrias que tardar en decirla: ")
cantidad = frase.split(" ")
cantidad_total = int(len(cantidad))
segundos = float(len(cantidad))/2
print(f"dijiste un total de {cantidad_total} de palabras y tardarias en decirlo un total de {segundos} segundos en decirla" )
if(segundos >= 60):
    print("flaco te dije que me digas una oracion no un testamento")
    
velocidad_de_dalto =float(2/1.3)

segundos_dalto = float(len(cantidad*100))//velocidad_de_dalto/100 
print(f"dalto tardaria un total de {segundos_dalto} segundos en decirla master")
