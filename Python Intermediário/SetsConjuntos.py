""" Sets em Python (Conjuntos) """
# Um Conjunto é uma coleção de elementos que você pode adicionar dentro de uma mesma estrutura de dados/ Algo bem similar as Listas 
#Porém a Maior Diferença entre os Sets/Conjuntos e as Listas,Tuplas ou Dicionários é: Sets só suportam elementos únicos
""" 
Funções dos Sets:
- Add (adiciona), ipdate (atualiza), clear, discard
- Union | (une)
- Intersection & (Todos os elementos presentes nos dois sets)
- Difference - (Elementos apenas no set da esquerda)
- Symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

"""

""" Criando Sets (2 Maneiras)"""
#Uma delas é bem parecido com dicionário, a diferença está que Sets não tem um Par de Chaves e Valor 
# Pois sets só recebem Valores
#Sets Não tem Índices, portanto não consigo ter acesso a um valor específico 
#Podemos Iterar sobre sets
"""-- 1 Maneira --"""
# s1 = {1,2,3,4}
# print(s1)
# print(type(s1))

"""-- 2 Maneira através da Função set() --"""
# s2 = set(1,2,3,4)


""" Se eu quiser Criar um Set Vazio função set() """
# set()


""" Adicionar Elementos no Set, utilizo a Função add(Value) e digo o Valor que eu quero adicionar"""
# s1 = {1,2,3,4}

# s1.add(5)
# s1.add((10,15,20))

# print(s1)


""" Removendo um Valor do Set Função .discard """
# s1 = {1,2,3,4}

# s1.discard(3)

# print(s1)


""" Função .update(), muito Similar a .add()"""
#A diferença é que ela recebe um iteravel e ela itera sobre ele.
# Está função não respeita ordem
# s1 = {1,2,3,4}

# s1.update('Lucas Santos')

# print(s1)


""" Não aceitam Elementos Duplicados """
# s1 = set()
# s1.update([1,2,3,4,5], {5,6,7,8})

# print(s1)


""" Se usar Sets para Eliminar Elementos Duplicados em uma Lista """
#No entanto, os elementos tem a saída fora de ordem
# l1 = [1,2,1,1,1,3,4,5,6,6,6,6,7,8,9,'Lucas', 'Santos', 'Santos']
# l1 = set(l1)    #Removeu todos Elementos Duplicados/ fazendo o Casting/Alterando sua tipagem / Com outro construtor
# l1 = list(l1)   #Retornei ela sendo uma Lista agora, sem os elementos Duplicados, pois foram corrigidos pelo set
# print(l1)


""" Função union ou | (Unior dois Sets)"""
#Ele elemina automaticamente as Repetições
# s1 = {1,2,3,4,5}
# s2 = {1,2,3,4,5,6}
# s3 = s1 | s2

# print(s3)


""" Função intersection() ou & (Retorna todos elementos Em Comum Entre Dois Sets) """
# s1 = {1,2,3,4,5}
# s2 = {1,2,3,4,5,6}
# s3 = s1 & s2    #Irá me retornar só os elementos em comum entre ambos

# print(s3) 


""" Função difference ou - (Retorna o valor do elemento da comparação entre ambos) """
""" Porém Contando da Esquerda, para Direita ou Seja, comparando o que tem no set da esquerda, que não tem no set da direita """
# s1 = {1,2,3,4,5}
# s2 = {1,2,3,4,5,6}
# s3 = s1 - s2

# print(s3)


""" Função symemtric_difference ou ^ (Retorna Todos Elementos diferentes entre ambos) """
# s1 = {1,2,3,4,5,7,8,9}
# s2 = {1,2,3,4,5,6}
# s3 = s1 ^ s2

# print(s3)


""" Utilizando Sets para Saber se uma Lista é Igual a Outra Lista, ou seja, tem elementos repetidos """
l1 = ['Lucas', 'Amira', 'Lineu', 'Lucas',]
l2 = ['Lucas', 'Amira', 'Lineu', 'Lucas',
'Lucas', 'Amira', 'Lineu', 'Lucas','Lucas', 'Lucas', 'Lucas']

if set(l1) == set(l2):
    print('É igual/ Mesmos Elementos')
else:
    print('Não tem os mesmos elementos é !')