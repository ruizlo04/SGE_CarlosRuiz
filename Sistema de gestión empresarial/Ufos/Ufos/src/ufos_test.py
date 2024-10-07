from ufos import *


avistamientos = lee_avistamientos('data/ovnis.csv')
for a in avistamientos:
    print(a)

print(duracion_total(avistamientos, 'CA'))  

print(comentario_mas_largo(avistamientos))

inicio = datetime.strptime('01/01/2000 00:00', '%m/%d/%Y %H:%M')
fin = datetime.strptime('01/01/2001 00:00', '%m/%d/%Y %H:%M')
print(avistamientos_fechas(avistamientos, inicio, fin))

print(hora_mas_avistamientos(avistamientos))
