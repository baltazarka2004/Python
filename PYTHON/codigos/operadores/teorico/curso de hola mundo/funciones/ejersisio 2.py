def igual (texto):
    cont = 0
    cantidad = len(texto)
    for i in range(cantidad):
        if texto[i] == texto[cantidad - i - 1]:
            cont += 1
    if cont == cantidad:
        return 1
    else:
        return 0

def es_palidromo(texto):
    s_texto = texto.replace(" ", "")
    s_texto.lower()
    
    val = igual(s_texto)
    if val == 1:
        return True
    else:
        return False

print("amo la paloma", es_palidromo("amo la paloma"))
        
    