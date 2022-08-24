""" Módulo Itertools - Combinations, Permutations e Product """
####### Essa é uma maneira bem simples de pegar combinações possiveis dentro de um Iteravel: Lista, Tupla etc.. #####
""" 

Combinations - Combinação - Ordem não importa
Permutations - Permutação - Ordem Importa 
Obs: Ambos não repetem valores únicos

Product - Produto - Ordem importa e repete valores únicos 
"""


""" Combinations """
""" Vamos Supor que eu queira Saber Todas as Combinações destas listas E (Não Importa a Ordem) 
"""
# Combinação pode ser de quantos você quiser ou seja, de 2 em Dois etc.. 

from itertools import combinations

pessoas = ['Lucas', 'Santos', 'Amira', 'Matheus', 'Lineu', 'Kaleu'] 

for grupo in combinations(pessoas, 2):  #Agora, iremos ter todas conbinações possiveis entre cada nome ex: ('Lucas', 'Santos') ('Lucas', 'Amira') etc.. 
    print(grupo)                        #Obs: A ordem não importa aqui ou seja, quando eu tenho uma combinação ex: ('Lucas', 'Santos'), não irá ter uma combinação de ('Santos', 'Lucas), pois ele trata isso da mesma forma




""" Permutations (Se a Ordem importar) """
# from itertools import combinations, permutations

# pessoas = ['Lucas', 'Santos', 'Amira', 'Matheus', 'Lineu', 'Kaleu'] 

# for grupo in permutations(pessoas, 2):   #Basta mudar aqui agora para Permutation onde a ordem irá improtar, onde ('Lucas', 'Santos') e ('Santos', 'Lucas), são valores diferentes
#     print(grupo)                       




""" Product (Todas as Combinações Possiveis, incluindo o próprio valor) """
# from itertools import product

# pessoas = ['Lucas', 'Santos', 'Amira', 'Matheus', 'Lineu', 'Kaleu'] 

# for grupo in product(pessoas, repeat=2):  #Preciso dizer quantas vezes eu quero que ele se repita/ fazer o repeat, neste caso será duas, grupos de 2
#     print(grupo)                        