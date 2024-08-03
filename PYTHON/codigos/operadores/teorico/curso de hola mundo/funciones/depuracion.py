def largo (texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado


print("chancho") #le agregamos un punto de quiebre "el punto rojo " para que la depuracion frene ahi
l = largo("hola mundo")
print(l)