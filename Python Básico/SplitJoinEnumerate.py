""" Split, Join, Enumerate """"""

* Split - Dividir uma string #str
* Join - Juntar uma lista #str
* Enumerate - Enumerar elementos da lista #Iterável

"""
from cmath import phase
from wsgiref.validate import validator


phrase = "O brasil é o país do futebol, o brasil é penta!"
# print(phrase)

# list = phrase.split(' ')  #Colocou a frase dentro de um array e a dividiu por espaço, tornando assim cada palvra separada por espaço, um valor.
# list2 = phrase.split(',')  #Agora a dividiu por , ou seja quando tiver uma , irá ser um valor.
# print(list) 
# print(list2) 

# print(len(phrase))  #Somou cada índice e espaço
# print(len(list))  #Somou por valores


# # Se eu quiser iterar sobre esta list
# for i, value in enumerate(list):  #Coloquei enumerate só para dar a visualização 
#     print(value, i) 

# """ Fazendo de uma forma mais direta """
# for value in list:
#     print(value)


# .count - Função que conta quantas vezes existe uma mesma palavra na frase
# for value in list:
#     print(value, list.count(value))

""" Fazendo um filtro do .count """
# word = ''
# score = 0

# for value in list2:
#     quantityX = list2.count(value)

#     if quantityX > score:
#         score = quantityX
#         word = value

# print(f'A palavra que apareceu mais vezes é: {word}, ({score}x)')


# Utilizando agora o .strip e .capitalize: Serve para remover o espaço do início e o final da String
""" Function Strip and Capitalize """
# for value in list2:
#     print(value.strip().capitalize()) #.capitalize: Deixa a primeira Letra da String maiúscula


# Function Join
# phrase = 'The Brazil It`s penta'
# list = phrase.split(' ')
# # print(list)

# phrase2 = ', '.join(list) #Aqui ele fez a junção das palavras que estavam divididas por elementos por conta do split, mas separando cada uma delas por , Porém mesmo assim unificando todas a somente 1 elemento agora.
# print(phrase2)

# print(phrase)
# print(list)
# print(phrase2)


""" Function Enumerate (Mais conhecido como desempacotador) Enumerar pacotes, através dos nossos índices"""
# phrase = 'The Brazil it`s penta!'
# list = phrase.split(' ')
# for indice, value in enumerate(list):
#     print(indice, value, list[indice]) 


""" One list can conter others lists  """
# list = [
#     [1,2],
#     [3,4],
#     [5,6],
# ]
# # print(list)

# for value in list:
#     print(value[0], value[1])  #Cada iteração do laço estou pegando o índice 0 e um do laço

""" Fazendo o desempacotamento Completo e de uma forma Direita """
# phrase2 = 'Não olhe mais atrás, mas sim sua visão tem que estar direcionada para frente, na direção do futuro.'
# listcuston = phrase2.split()

# together = ' '.join(listcuston)
# print(phrase2)
# print(listcuston)
# print(together)

""" Outra forma """
# list = ['Santos', 'Amira', 'Lineu']

# n1, n2, n3 = list   

# print(n1)


""" Desempacotamento Correto! """
# vendedores = ['Marcus', 'Amanda', 'Ale', 'Carol']
# vendas = [15,20,10,30]

# for vendedor in vendedores:
#     print(vendedor)

# tamanho_lista = len(vendedores)
# for i in range(tamanho_lista):
#     print(vendedores[i], end=' ')
#     print(vendas[i])


# for i, vendedor in enumerate(vendedores):
#     print(vendedor, end=' ')
#     print(vendas[i])

# Outra forma:

# for vendedor, venda in zip(vendedores,vendas):
#     print(vendedor, end=' ')
#     print(venda)


""" Falando um Pouco mais sobre Enumerate """
"""---- No entando, vamos falar de list Primeiro ---- """
# Sabemos que uma lista é um conjunto de Elementos, e uma lista, pode conter outras 


list = [
        #0         #1      #2
    ['Santos', 'Amira', 'Lineu'],   #0
    ['Matheus', 'Kaleu', 'Dominic'],   #1
    ['Guendolff','hobbit', 'Sauron'],   #2
]

# print(list[1][2])

# listNumbered = enumerate(lista) 

# print(list(listNumbered))  #Aqui fizemos o typequest, convertemos de um objeto para uma list


""" Complexo Pra caramba, mas da para ler """
for value in enumerate(list):
    value_numbered, mylist = value
    name1, name2, name3 = mylist    
    print(name1)
    print(value_numbered)
    print(mylist)