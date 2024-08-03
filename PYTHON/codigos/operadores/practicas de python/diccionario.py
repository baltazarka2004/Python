def diccionario(oracion):
    separada = oracion.split(" ")
    longi = map(len, separada)
    return dict(zip(separada, longi))
    
    
    
print(diccionario ("      "))
    
