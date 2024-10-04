

import csv 
from datetime import datetime
from math import sqrt
from collections import namedtuple

Avistamiento = namedtuple('Avistamiento', 'fechahora, ciudad, estado, forma, duracion, comentarios, latitud, longitud')
# Test de la función lee_avistamientos
def lee_avistamientos(fichero):
    res= []
   
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for x in lector:
            fecha_hora = x[0]
            fechahora = datetime.strptime(fecha_hora, '%m/%d/%Y %H:%M')
            ciudad = x[1]
            estado = x[2]
            forma = x[3]
            duracion = int(x[4])
            comentarios = x[5]
            latitud= float(x[6])
            longitud= float(x[7])
            res.append(Avistamiento(fechahora, ciudad, estado, forma, duracion, comentarios, latitud, longitud))

    return res  
#Test de la función duracion_total
def duracion_total(avistamientos, estado):
    res = 0
    for r in avistamientos:
        if r.estado == estado:
            res += r.duracion
    return res

    
# Test de la función comentario_mas_largo



# Test de la función avistamientos_fechas



# Test de la función hora_mas_avistamientos











