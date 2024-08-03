print ("""calculadora en python
para salir escriba salir
las operaciones aceptadas son la suma, resta, multi y div""")

resultado = int(input("escriba su primer numero: "))
op = input("escriba la operacion: ")
while op.lower() != "salir":
    num2 = int(input("ingrese el siguiente numero: "))
    if op.lower() == "suma":
        resultado += num2
    elif op.lower() == "resta":
        resultado  -= num2
    elif op.lower() == "multi":
        resultado *= num2
    elif op.lower() == "divi":
        resultado  /= num2
    else:
        print("operacion no valida")
           
    print(f"el resultado es:",resultado)
    op = input("escriba la operacion:")
    
    
        
    

