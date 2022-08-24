""" Como criar Pacotes e Módulos em Python """
# import vendas.CalculaPrice

# price = 49.90
# price_increase = vendas.CalculaPrice.increase(price, 15)   #Estou falando o preço e a porcentagem que eu quero que aumente deste valor
# price_increase = vendas.CalculaPrice.increase(value=price, percentage=15)   #Posso falar de forma nomeada também
# print(price_increase)

""" De uma Forma Direta (Menos código e continua fácil de ler) """
# from vendas import CalculaPrice   #Estou importando o Módulo CalculaPrice completo, desta forma. Tornando não necessário utilizar vendas.
# price = 49.90
# price_increase = CalculaPrice.increase(price, 15)   #Estou falando o preço e a porcentagem que eu quero que aumente deste valor
# price_increase = CalculaPrice.increase(value=price, percentage=15)   #Posso falar de forma nomeada também
# print(price_increase)


""" De forma Mais Simplificada ainda 100% """
from vendas.CalculaPrice import increase, reduction
# from vendas.formata import price #meu price-> 

price = 49.90  #Esta sobescrevendo aqui <-
#Para arrumar isso:
from vendas.formata.price import realbr #Dessa forma meu realbr

price_increase = increase(value=price, percentage=15, formata=True)   #Posso falar de forma nomeada também
print(price_increase)

price_reduction = reduction(value=price, percentage=15, formata= True)   #Posso falar de forma nomeada também
print(price_reduction)

print(realbr(59.95))