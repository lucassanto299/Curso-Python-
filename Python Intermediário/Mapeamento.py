""" Para eu importar os dados do Arquivo Map, para meu Mapeamento """
""" 
Muitas quando você trabalha com dados, você precisa mapear esses dados, alterar eles
Uma das formas é List Comprehension
Função Map: Fica mais interessante com dicionários
"""
from FuncaoMap import products, people, lista    #Acabei de importar os dados 

# print(lista)  #importei minha lista que esta no arquivo FunçãoMap

# Agora digamos que eu queria multiplicar por 2 cada elemento que esta dentro da minha lista
# Podemos fazer isso através da função Map

""" Função Map """
""" 
A função map é um pouco diferente das outras funções, porque ela recebe como argumento, uma outra função
Por isso, utilizamos a função lambda, para o primeiro argumento
- A função Map, não retorna uma lista pronta, ela retorna um iterador, para você iterar sobre o elemento. Portanto, para ver sua saída, converta(type casting) ou faça um for.
"""
# nova_lista = map(lambda x: x * 2, lista)   #O primeiro argumento que minha função map recebe é uma função, passei o lambda, escolher uma variavel para receber cada elemento da nossa lista que é X e deste X, eu quero que me retorne x * 2, e como ultimo argumento, eu passo a minha própria lista
# print(lista)                                          #Isso é muito similar a List Comprehension, por conta do papel do for, só que aqui é o map, pegando cada elemento da lista
# print(list(nova_lista))   #Converti minha lista que é um objeto de mapeamento, para uma list propiamente dita

# """ Só que isso fica bem melhor em (List Comprehension) """
# nova_lista = [x *2 for x in lista]
# print(lista)
# print(nova_lista)


""" Função Map com (Dicionários) onde ela fica realmente interessante, pois fica melhor ao inves de usar List Comprehension """

# Ex: Queres um dicionários que tenha somente os preços dos produtos
# preco = map(lambda value: value['Price'], products)   #A expressão lambda, só funciona para expressões ou seja se eu quisesse somar, colocar 5% a mais no valor de cada produto, sem alterar o restante da estrutura, não daria

# for precos in preco:
#     print(precos)


""" Exemplo 1 """
# A expressão lambda, só funciona para expressões ou seja se eu quisesse somar, colocar 5% a mais no valor de cada produto, sem alterar o restante da estrutura, não daria
# Para fazer isso, precisamos definir uma função ex: Aumenta preço, esta função vai receber um produto:

# Conclusão: A função Map: Ela esta mapeando uma função, que passa em cada elemento do meu iteravel (list, dict), que neste caso é minha list de Products

# def aumenta_preco(produto): # A cada linha da minha lista de produtos, está chegando aqui no meu Parâmetro (produto)
#     produto['Price'] = round(produto['Price'] * 1.5, 2)   #Desse argumento, eu acessei a chave[Price] e ai eu modfiquei o valor desta Chave Price
#     return produto   #Assim que eu modifiquei o valor, ao inves de retornar só a produto[Price], eu retornei a linha inteira de produto, com o valor já modficado


# novos_precos = map(aumenta_preco, products)  #Agora minha linha inteira foi alterada e salva aqui no meu dicionário

# for produto in novos_precos:   #E aqui fizemos um for nele, para ficar melhor a visualização e resolveu este valor
#     print(produto)


""" Fazendo Agora com o Nome das Pessoas, que estão dentor do meu dicionário """
# Ou seja, criar uma lista só com o nome das Pessoas que estão dentro do meu dicionário |Poderia fazer com list comprehension, mas vamos fazer com map 
# nomes = map(lambda name:name['Name'], people)  #Novamente, estamos passando uma função, para cada elemento da minha lista, e eu retorno o que eu desejar, poderia ser ages etc.., poderia alterar o valor da idade também etc..

# for nome in nomes:
#     print(nome)

""" Pode ser com idade também, Vou criar uma nova chave e colocar dentro do meu dicionário (Só para brincar)"""
# def aumenta_idade(pessoa):
#     pessoa['nova_idade'] = round(pessoa['Ages'] * 1.20)  # Passando nosso novo dicionário 
#     return pessoa

# nomes = map(aumenta_idade, people) 

# for nome in nomes:
#     print(nome)
