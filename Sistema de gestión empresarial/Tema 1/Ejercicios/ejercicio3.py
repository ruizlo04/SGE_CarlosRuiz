def relacion(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0
    
print(relacion(5, 10))
print(relacion(3, 3))
print(relacion(2, 1))