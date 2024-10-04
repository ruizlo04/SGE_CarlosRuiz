def separar(lista):
    pares = []
    impares = []
    
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    
    pares.sort()
    impares.sort()
    
    return pares, impares

pares, impares = separar([5, 2, 6, 7, 1])
print(pares)  
print(impares) 