""" Groupby - Agrupando Valores / Agrapando Elementos em Python """
# É comum em Python vermos algo do tipo: Uma lista de Alunos e com dicionários
# E neste caso, eu gostaria de Ordenar por Nota
# from itertools import groupby,tee    #Essa função groupby precisa que o dicionários este ordenado ou seja, se eu quiser agrupar pela nota, eu precisaria que todas as notas tivessem em ordem ex: A A A B B B C C C

# alunos = [
#     {'Nome': 'Lucas', 'Nota': 'A'},
#     {'Nome': 'Lineu', 'Nota': 'B'},
#     {'Nome': 'Amira', 'Nota': 'D'},
#     {'Nome': 'Matheus', 'Nota': 'C'},
#     {'Nome': 'Kaleu', 'Nota': 'A'},
#     {'Nome': 'Natalia', 'Nota': 'B'},
#     {'Nome': 'Luana', 'Nota': 'C'},
# ]

# alunos.sort(key = lambda item: item['Nota'])  #Neste caso já daria para ver de forma ordenada, mas queremos agrupar em um dicionário todos alunos por classificação de um dicionário que tem todos alunos da mesma Nota

# # Vou fazer um for, só para ficar melhor a visualização
# for value in alunos:
#     print(value)



""" Agrupando Todos Alunos Por Nota em um Dicionário """
# alunos = [
#     {'Nome': 'Lucas', 'Nota': 'A'},
#     {'Nome': 'Lineu', 'Nota': 'B'},
#     {'Nome': 'Amira', 'Nota': 'D'},
#     {'Nome': 'Matheus','Nota': 'C'},
#     {'Nome': 'Kaleu', 'Nota': 'A'},
#     {'Nome': 'Natalia','Nota': 'B'},
#     {'Nome': 'Luana', 'Nota': 'C'},
# ]

# ordena = lambda item: item['Nota']
# alunos.sort(key= ordena)
# alunos_AgrupadosNota = groupby(alunos, ordena)

# for agrupamento, valores_agrupados in alunos_AgrupadosNota:
#     print(f'Agrupamento: {agrupamento}')

#     for aluno in valores_agrupados:
#         # quantidade = len(list(valores_agrupados))
#         # print(f'{quantidade} alunos que tiraram a Nota {agrupamento}') 
#         print(aluno)
#     print()


""" Se eu desejar selecionar por Número de alunos por cada nota referente """
# alunos = [
#     {'Nome': 'Lucas', 'Nota': 'A'},
#     {'Nome': 'Lineu', 'Nota': 'B'},
#     {'Nome': 'Amira', 'Nota': 'D'},
#     {'Nome': 'Matheus','Nota': 'C'},
#     {'Nome': 'Kaleu', 'Nota': 'A'},
#     {'Nome': 'Natalia','Nota': 'B'},
#     {'Nome': 'Luana', 'Nota': 'C'},
# ]

# ordena = lambda item: item['Nota']
# alunos.sort(key= ordena)
# alunos_AgrupadosNota = groupby(alunos, ordena)

# for agrupamento, valores_agrupados in alunos_AgrupadosNota:
#     print(f'Agrupamento: {agrupamento}')
    
#     quantidade = len(list(valores_agrupados))  #Aqui estou fazendo por quantidade de alunos por nota
#     print(f'{quantidade} alunos que tiraram a Nota {agrupamento}')  


""" Forma Completa de Fazer Isso """
# from itertools import groupby,tee 

# alunos = [
#     {'Nome': 'Lucas', 'Nota': 'A'},
#     {'Nome': 'Lineu', 'Nota': 'B'},
#     {'Nome': 'Amira', 'Nota': 'D'},
#     {'Nome': 'Matheus','Nota': 'C'},
#     {'Nome': 'Kaleu', 'Nota': 'A'},
#     {'Nome': 'Natalia','Nota': 'B'},
#     {'Nome': 'Luana', 'Nota': 'C'},
# ]

# ordenada = lambda item: item['Nota'] 
# alunos.sort(key= ordenada)
# alunos_agrupados = groupby(alunos, ordenada)   #Estou passando para dentro da função groupby, que eu quero que ele pegue meu dicionário de alunos, porém deste dicionário, eu quero a chave Nota, que está dentro da minha variavel ordenada

# for agrupamento, valores_agrupados in alunos_agrupados:
#     v1, v2 = tee(valores_agrupados)
#     print(f'Agrupamento: {agrupamento}')
    
#     quantidade = len(list(v2))
#     print(f'\t{quantidade} Alunos que tiraram {agrupamento}')

#     for aluno in v1:
#         print(f'\t{aluno}')



""" Sem a função tee """
# from itertools import groupby

# alunos = [
#     {'nome': 'Luiz', 'nota': 'A'},
#     {'nome': 'Letícia', 'nota': 'B'},
#     {'nome': 'Fabrício', 'nota': 'A'},
#     {'nome': 'Rosemary', 'nota': 'C'},
#     {'nome': 'Joana', 'nota': 'D'},
#     {'nome': 'João', 'nota': 'A'},
#     {'nome': 'Eduardo', 'nota': 'B'},
#     {'nome': 'André', 'nota': 'C'},
#     {'nome': 'Anderson', 'nota': 'B'},
# ]

# def ordena(item):
#   return item['nota']

# alunos.sort(key=ordena)
# alunos_agrupados = groupby(alunos, ordena)

# # Sem tee (com list)
# for agrupamento, valores_agrupados in alunos_agrupados:
 
#   valores = list(valores_agrupados)
#   print(f'Agrupamento: {agrupamento}')
  
#   for aluno in valores:
#     print(f'\t{aluno}')
  
#   quantidade = len(valores)
#   print(f'\t{quantidade} alunos tiraram nota {agrupamento}')