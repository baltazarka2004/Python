nombre = input("como te llamas?: ")
edad = input("cual es tu edad: ")
dire = input("donde vives:")
num = input("cual es tu numero: ")
datos = {"nombres": nombre, "edad": edad, "dire": dire, "num": num }
print(datos["nombres"], "tiene", datos["edad"], "y vive en", datos["dire"], ",\nsu numero es: ", datos["num"])



