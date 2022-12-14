from got import *

def test_lee_batallas(batallas):
    print('El último elemento de la lista es:',batallas[-1])

def test_reyes_mayor_menor_ejercito(batallas):
    rmme=reyes_mayor_menor_ejercito(batallas)
    print('El rey con el mayor ejército es {}, y el rey con el menor ejército es {}.'.format(*rmme))

def test_batallas_mas_comandantes(batallas,regiones=None,n=None):
    bmc=batallas_mas_comandantes(batallas,regiones,n)
    print(f'Las {n} batallas con más comandantes en {regiones} son {bmc}.')

def test_rey_mas_victorias(batallas,rol='ambos'):
    rmv=rey_mas_victorias(batallas,rol)
    print(f'El rey con mas victorias en el rol de {rol} (entendiendo "ambos" por atacante y atacado) es {rmv}.')

def test_rey_mas_victorias_por_region(batallas,rol='ambos'):
    rmvpr=rey_mas_victorias_por_region(batallas,rol)
    print(f'El rey con mas victorias en el rol de {rol} (entendiendo "ambos" por atacante y atacado) por cada región es {rmvpr}.')

def main():
    DATOS = lee_batallas('./data/battles.csv')
    #test_lee_batallas(DATOS)
    test_reyes_mayor_menor_ejercito(DATOS)
    #test_batallas_mas_comandantes(DATOS,{'The North', 'The Riverlands'},4)
    #test_rey_mas_victorias(DATOS,'ambos')
    #test_rey_mas_victorias_por_region(DATOS,'ambos')



if '__main__'==__name__:
    main()
