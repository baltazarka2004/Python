import math
pi = math.pi
base = float(input("ingresar base del rectangulo: "))
altura = float(input("ingresar altura del rectangulo: "))
def perimetro():   
    peri = (base*2)+(altura*2)
    print("el perimetro del rectangulo es de: "+str(peri))
    area_rec()
    
def area_rec():
    area = base*altura 
    print("el area del rectangulo es de: "+ str(area))
    
perimetro()



# Calcular el área de un rectángulo (alineado con los ejes 𝑥 e 𝑦) dadas sus coordenadas
#𝑥1, 𝑥2, 𝑦1, 𝑦2.

def area_2():
    x1 = float(input("ingrese cordenada de x1: "))
    x2 = float(input("ingrese cordenada de x2: "))
    y1 = float(input("ingrese cordenada de y1: "))
    y2 = float(input("ingrese cordenada de y2: "))
    base = abs(x2-x1)
    altura = abs(y2-y1)
    return base*altura
area=area_2()
print("el area del rectangulo es :"+str(area))


#calcular el radio de un circulo dado su radio
radio = float(input("ingresar radio del cierculo: "))
def perimetro_circulo():
    
    return 2*radio*pi
c_peri = perimetro_circulo()
c_peri = format(c_peri,".2f")
print("el valor del perimetro del circulo es de: "+str(c_peri))


#volumen del circulo

#volumen=4/3*PI*r(al cubo)

def volumen_c():
    radio_3 = radio
    for x in range (1,3):
        radio_3 = radio_3*radio
    return (4/3)*pi*radio_3

volumen = volumen_c()
volumen = format(volumen,".2f")
print("el volumen del circulo es de :",volumen)

#calcular hipotenusa de un triangulo rectangulo

print("ingresar 2 catetos del triangulo rectangulo: ")
c1 = float(input("cateto 1: "))
c2 = float(input("cateto 2: "))
def hipo():
    hipotenusa = (c1*c1)+(c2*c2)
    return hipotenusa

hipotenusa = hipo()
hipotenusa = format(hipotenusa,".2f")
print("la hipotenusa del triangulo es: "+str(hipotenusa))
    

