""" Função Filter (Serve para Filtrar coisas) """
""" 
Função filter: Também recebe uma função como parâmetro, assim como o Map
A diferença do Filter para o Map: É que ela vai lhe retornar True ou False, para a expressão que você falar ou seja, os que retornam falso, são os que eu não quero que meu filter pegue e eles serão automaticamente eliminados
E ela vai me retornar um Iterator sempre, por isso é preciso converter.
"""
from Mapeamento import lista, products, people
# Vamos criar uma nova list ou novo dicionário e filtrar algo que está lá dentro

# new_list = filter(lambda value: value < 5, lista)

# print(list(new_list))

""" Isso poderia ser feito com List Comprehension também """
# new_list = [value for value in lista if value < 5]
# print(new_list)


""" Pegando um Dado um Pouco mais Complexo, ex: Produtos, em que os valores sejam maiores que 10 """
# new_list = filter(lambda value: value['Price'] > 50, products)

# #Como iremos ter um dicionário, irei utilizar o For para ficar melhor a visualização também
# for produtos in new_list:
#     print(produtos)   


""" Se for preciso fazer algo mais complexo com Filter, podemos utilizar uma função por fora também, assim como Map """
# E a vantagem de utilizar funções ao invés da lambda, é que você pode reutilizar o Código em outros Locais
# def filtra(produto):
    # if produto['Price'] > 50:
    #     return True
    # else:
    #     return False
    # Ou, e se eu quiser posso criar uma nova Chave[], Mas ai perde o sentido de ser filter, é melhor então um map, mas da.

    # if not produto['Price'] < 50:
    #     produto['É_Caro'] = True  # Todo produto que o valor for maior que 50, eu estou criando uma nova chave para ele com nome [É_caro] e com o valor da Chave sendo True
    #     return True
    
    # else:
    #     return False

# new_list = filter(filtra, products)

# for produtos in new_list:
#     print(produtos)   


""" Filtrando quem é Maior de Idade """
#Só vale a pena se for reutilizar em outra parte do Código
# def filtro(pessoa):
#     if pessoa['Ages'] >= 18:
#         return True

# new_list = filter(filtro, people)

# for idade in new_list:
#     print(idade)

""" Ou """
# new_list = filter(lambda pessoa: pessoa['Ages'] >= 18, people)

# for idade in new_list:
#     print(idade)