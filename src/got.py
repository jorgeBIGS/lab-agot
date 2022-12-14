from collections import namedtuple,Counter,defaultdict
import csv
from parsers import *

BatallaGOT = namedtuple('BatallaGOT', 'nombre, rey_atacante, rey_atacado, gana_atacante, muertes_principales, comandantes_atacantes, comandantes_atacados, region, num_atacantes, num_atacados')

def lee_batallas(archivo):
    result=[]
    with open(archivo, encoding='utf-8') as f:
        lector=csv.reader(f)
        next(lector)
        for nombre, rey_atacante, rey_atacado, gana_atacante, muertes_principales, comandantes_atacantes, comandantes_atacados, region, num_atacantes, num_atacados in lector:
            gana_atacante=parsear_gana_atacante(gana_atacante)
            muertes_principales=parsear_muertes_principales(muertes_principales)
            comandantes_atacantes=parser_list(comandantes_atacantes)
            comandantes_atacados=parser_list(comandantes_atacados)
            num_atacantes=parser_int(num_atacantes)
            num_atacados=parser_int(num_atacados)
            result.append(BatallaGOT(nombre, rey_atacante, rey_atacado, gana_atacante, muertes_principales, comandantes_atacantes, comandantes_atacados, region, num_atacantes, num_atacados))
    return result

def ejercito_rey(batallas):
    result=defaultdict(int)
    for b in batallas:
        if b.num_atacantes!=None:
            result[b.rey_atacante]+=b.num_atacantes
        if b.num_atacados!=None:
            result[b.rey_atacado]+=b.num_atacados
    return result

def reyes_mayor_menor_ejercito(batallas):
    result=ejercito_rey(batallas).items()
    maxrey=max(result,key=lambda x:x[1])[0]
    minrey=min(result,key=lambda x:x[1])[0]
    return (maxrey,minrey)

def filtrar_regiones(batallas,regiones):
    if regiones!=None:
        return [b for b in batallas if b.region in regiones]
    else:
        return batallas

def comandante_en_mas_batallas(batallas):
    result = defaultdict(int)
    for b in batallas:
        for c in b.comandantes_atacantes:
            result[c] +=1
    return result

def batallas_mas_comandantes(batallas,regiones=None,n=None):
    data=filtrar_regiones(batallas,regiones)
    data=sorted(data,key=lambda x:(len(x.comandantes_atacantes+x.comandantes_atacados)),reverse=True)
    result=[(d.nombre,len(d.comandantes_atacantes+d.comandantes_atacados)) for d in data]
    if n!=None:
        return result[:n]
    else:
        return result

def rey_mas_victorias(batallas,rol='ambos'):
    result=defaultdict(int)
    if rol!='atacado':
        for b in batallas:
            if b.gana_atacante==True:
                result[b.rey_atacante]+=1
    if rol!='atacante':
        for b in batallas:
            if b.gana_atacante==False:
                result[b.rey_atacado]+=1
    return max(result.items(),key=lambda x:x[1])[0]

def conjunto_regiones(batallas):
    return {b.region for b in batallas}

def rey_mas_victorias_por_region(batallas,rol='ambos'):
    result={}
    regiones=conjunto_regiones(batallas)
    for region in regiones:
        datos=filtrar_regiones(batallas,region)
        reymas=rey_mas_victorias(datos,rol)
        result[region]=reymas
    return result
