def recortar(a, b, c):
    if a < b:
        return b
    elif a > c:
        return c
    else:
        return a
    
print(recortar(15, 0, 10))