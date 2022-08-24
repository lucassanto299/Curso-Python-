""" Função Reduce em Python """
""" 
Essa função não vem por Padrão no Python, portanto é preciso importar ela
A função Reduce: É uma Acumuladora, ou seja, ela vai fazer a acumulação de valores
Ela recebe como Parâmetro uma função também, assim como Filter e Map
"""
from functools import reduce
from FuncaoMap import products, people, lista

""" Só para Lembrar """
#Isso é um Acumulador, estamos somando todos valores e reduzindo todos esses valores em um Valor apenas.
#Por isso ela se chama Reduce, pois ela reduz, retornando apenas um Valor
# acc = 0
# for value in lista:
#     acc += value

# print(acc)

""" Função reduce """
 #Meu acc será meu acumulador, 
 # O value será o parâmetro para cada valor da minha lista, que eu farei a soma com meu acc, 
 # chamo a minha lista para jogar estes valores no parâmetro e ao final digo o valor que eu desejo que comece o acc
# soma_lista = reduce(lambda acc, value: value + acc, lista, 0)

# print(soma_lista)


""" Função Reduce com Dicionários (A Soma Total de Produtos) """
# soma_Price_produtos = reduce(lambda acc, value: round(value['Price'] + acc, 2), products, 0)
# #Se eu desejar a média de preço entre todos meus produtos: Soma dos preços do Produto / pela quantidade Total de produtos 
# print(f'Soma dos Produtos: {soma_Price_produtos}, Média de Valores: {round((soma_Price_produtos / len(products)),2)}')    


""" Ex 2: Media das Idades de Pesoas """
# soma_idades = reduce(lambda acc, value: value['Ages'] + acc, people, 0)
# # Para saber a media de idades, eu preciso saber a soma total de todas idades / Número de pessoas Totais
# print(f'Media da idade de Pessoas nesta lista: {int(soma_idades / len(people))}')