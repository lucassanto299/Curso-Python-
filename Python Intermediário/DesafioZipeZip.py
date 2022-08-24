""" Desafio Zip (Retorna um Iterador que tem o Next, e não um gerador) """
"""  
Considerando Duas Listas de inteiros ou floats (Lista A e Lista B)
Some os Valores nas Listas Retornando uma nova Lista com os Valores Somados:

Se uma Lista for maior que a outra, a soma só vai considerar o tamanho da menor.

Exemplo:
lista_A = [1,2,3,4,5,6,7]
lista_B = [1,2,3,4,]

========================== Resultado
lista_soma = [2,4,6,8]

"""
lista_A = [1,2,3,4,5,6,7]
lista_B = [1,2,3,4,]

soma = [value + value2 for value, value2 in zip(lista_A, lista_B)]
print(soma)
print(list(zip(lista_A, lista_B)))   #Só para mostrar o que esta acontecendo

""" 2 Forma (Resolver) """
# lista_A = [1,2,3,4,5,6,7]
# lista_B = [1,2,3,4,]

# listaA_B = zip(lista_A, lista_B)

# soma = [sum(value) for value in listaA_B]
# print(soma)

""" 3 Forma (Resolver) """
# lista_A = [1,2,3,4,5,6,7]
# lista_B = [1,2,3,4,]

# list_soma = []

# for i in range(len(lista_B)):
#     list_soma.append(lista_A[i] + lista_B[i])

# print(list_soma)

""" 4 Forma (Resolver) """
# lista_A = [1,2,3,4,5,6,7]
# lista_B = [1,2,3,4,]

# lista_soma = []

# for i, _  in enumerate(lista_B):   # _ Signica que eu não quero algo, exemplo: uma tupla, eu não quero o valor, neste caso, só o indice, ai utiliza _
#     lista_soma.append(lista_A[i] + lista_B[i])  
#     print(lista_soma)


""" 5 Forma (resolver) """
""" 
O problema é que zip só une as listas até o tamanho da menor lista (como proposto no exercício).

Uma outra possibilidade é usar zip_longest para capturar os valores da lista maior.
A ideia é a mesma, veja:
"""
# from itertools import zip_longest
 
# lista_a = [10, 2, 3, 4, 5]
# lista_b = [12, 2, 3, 6, 50, 60, 70]
# lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
# print(lista_soma)  # [22, 4, 6, 10, 55, 60, 70]

""" 
Neste caso, usamos o "fillvalue" como 0 (zero), assim conseguimos 
capturar os valores restantes da lista maior, 
realizando contas, sem obter um erro em nosso programa.
"""