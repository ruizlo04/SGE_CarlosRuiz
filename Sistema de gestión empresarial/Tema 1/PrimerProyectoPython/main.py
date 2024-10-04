
print("Hola mundo")

print(2+3)
print(2-3)
print(2*3)
print(2/3)
print(2**3)

res = None
res = 3
print(res)

cadena_salto_de_linea = "Hola\nMundo"
print(cadena_salto_de_linea)
cadena_tabulador = "Hola\tMundo"
print(cadena_tabulador)

def nombre_funcion (parametro1):
    res = "Jose Luis"
    return res 
print(nombre_funcion(res))

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
r = [a,b,c]

print(r)
print(r[0][0:3])

nombre = input("¿Cual es tu nombre?")

print("Hola", nombre, "¿Cómo estás?")

print(1+1 == 3)

numeros = [1,2,3,4,5,6,7,8,9,10]
indice = 0
while indice < len(numeros):
    print(numeros[indice])
    indice+=1

cadena = "Hola"
for l in cadena: 
    print(l)