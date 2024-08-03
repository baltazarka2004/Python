#SET = grupo o conunto

#set = coleccion de datos que no se peude repetir ni esta ordenada

primer = {1, 1, 2, 2, 3, 4}

print(primer) # el numero 1 y 2 que estaba duplicado no lo imprime
# los remueve
segundo = [3, 4, 5]
segundo = set(segundo) #set resive un iterable
print(primer | segundo) #hace una union
print(primer & segundo) #me muestra los elementos que esten tanto en el priemr set com en el segudno set
print(primer - segundo) #borra los elementos del primer set que esten ene el segudno, osea si hay un 1 y uin 2 en el priemro y ene le segudno hay un 2 y 4 borrara el dos pq esta en el segudno
print(primer ^ segundo) #muestra los que no esten duplicados entre los sets


if 5 in segundo:
    print("hola muidno")
