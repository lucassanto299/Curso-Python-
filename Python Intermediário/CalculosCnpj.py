import re

regressivos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def valida(cnpj):
    cnpj = apenas_numeros(cnpj)

    try:
        if verificar_sequencia(cnpj):
            print('É uma sequencia')
            return False
    except:
        return False
    
    try:
        novo_cnpj = calcula_digito(cnpj=cnpj, digito=1)
        novo_cnpj = calcula_digito(cnpj=cnpj, digito=2)
    except Exception as e:
        return False
    
    if novo_cnpj == cnpj:
        return True
    else:
        return False


def calcula_digito(cnpj, digito):
    if digito == 1:
        regressivo = regressivos[1:]
        novo_cnpj = cnpj[:-2]
    
    elif digito == 2:
        regressivo = regressivos
        novo_cnpj = cnpj
    else:
        return None
    
    total = 0

    for indice,value in enumerate(regressivo):
        total += int(cnpj[indice]) * value
    
    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0
   
    return f'{novo_cnpj}{digito}'
    

def apenas_numeros(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def verificar_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    if sequencia == cnpj:
        return True
    else:
        return False