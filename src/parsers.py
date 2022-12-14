def parsear_gana_atacante(gana_atacante):
    return gana_atacante.strip().lower() == 'win'

def parsear_muertes_principales(muertes_principales):
    return muertes_principales.strip() == '1'

def parser_list(cad):
    return [c.strip() for c in cad.split(',')] 

def parser_int(num):
    result = None
    if num!='':
        result = int(num)
    return result