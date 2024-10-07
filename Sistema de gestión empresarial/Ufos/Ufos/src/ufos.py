

import csv 
from datetime import datetime
from math import sqrt
from collections import namedtuple

Avistamiento = namedtuple('Avistamiento', 'fechahora, ciudad, estado, forma, duracion, comentarios, latitud, longitud')
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
            res += float(r.duracion)
    return res

    
# Test de la función comentario_mas_largo
def comentario_mas_largo(avistamientos):
    res = ''
    maximo = 0
    for r in avistamientos:
        if len(r.comentarios) > maximo:
            maximo = len(r.comentarios)
            res = r.comentarios
    return res


# Test de la función avistamientos_fechas
def avistamientos_fechas(avistamientos, inicio, fin):
    res = []
    for r in avistamientos:
        if r.fechahora >= inicio and r.fechahora <= fin:
            res.append(r)
    return res


# Test de la función hora_mas_avistamientos
def hora_mas_avistamientos(avistamientos):
    res = {}
    for r in avistamientos:
        if r.fechahora.hour in res:
            res[r.fechahora.hour] += 1
        else:
            res[r.fechahora.hour] = 1
    maximo = 0
    hora = 0
    for k, v in res.items():
        if v > maximo:
            maximo = v
            hora = k
    return hora













