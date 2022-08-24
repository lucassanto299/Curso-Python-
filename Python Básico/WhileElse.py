# While / else

""" 
Contadores
Acumuladores

Obs: O laço while precisa sempre de um número/contador.Pois 
este contador, irá garantir que nosso laço tenha um fim.
"""

contador = 1 
acumulador = 1

while contador <= 10:
    print(contador, acumulador)
    
    if contador > 5:
        break
    acumulador = acumulador + contador
    contador += 1 
else:
    print('Sai fora!')