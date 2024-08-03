def main():
    print("vamos a a crear una conventor de kilometros a millas,pies y pulgadas")
    
    def metros():
        metro = float(input("ingresar la medida en kilometros: "))
        return metro
    medida = metros()
    def convertor(metro):
        print("valor e milla:",format(metro*1.6,".2f"))
        print("valor e milla:",format(metro*30.48*100000,".2f"))   #utilizo "format" par alimitar la parte fraccionaria
        print("valor e milla:",format(metro*2.54*100000,".2f"))
    convertor(medida)
          
main()

        
        
    
    