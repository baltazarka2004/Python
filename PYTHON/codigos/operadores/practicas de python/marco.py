
def mensaje():
    print("hoy haremos una calculadora de cauntas piajs puede llegar a chupar marco")
    
pijas = 0
pijas = int(pijas)
def cal ():
    total = 0
    pijas = int(input("cuantas piajs chupo hoy marco?: "))  
    while True: 
        if pijas != 0:
            print(f"exelente entonces marco hoy a chupado {pijas} pijas\n vamos a hacer el calculo porque por si no lo sabias , marco segun el dia tiene UN MULTIPLICADOR!!!")
            print("los lunes martes y viernes hay un multiplicador por 3\nlos miercoles y jueves por 2\n y los sabdos y domingos guardo todas sus energias y se multiplica POR 5!!!!!!")
        else:
            print("marco hoy no a chupado pijas :(")
            break
        
        mult = dias(input("que dia chupo marco todas estas pijas?: "))
        while mult != 0:
            input()
            pijas *= mult
            print (f"con el multiplicador de pijas , marcos chupo un total de {pijas} pijas")  
            total += pijas
            mult = 0
        pijas = int(input("cuantas otras pijas morfo el socotroco de marcos: "))
        

            
def dias(dia):
    dia = dia.lower()
    if dia == "lunes" or dia == "martes" or dia == "viernes":
        return 3
    elif dia == "miercoles" or dia == "jueves": #aca vamos a ponjer el multiplicador
        return 2
    elif dia == "sabado" or dia == "domingo":
        return 5
    else:
        print("Día no válido.")
        return 0
        
        
        
mensaje()
cal()

