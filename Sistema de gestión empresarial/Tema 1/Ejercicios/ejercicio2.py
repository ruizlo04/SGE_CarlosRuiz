import math

def area_circulo(radio):
    return radio**2*math.pi

radio = 5.0
area = area_circulo(radio)

print("El área del círculo es", round(area, 2))