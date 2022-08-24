""" Dictionary Comprehension e Sets em Python """
# lista = [
#     ('Chave', 'Valor'),
#     ('Chave2', 'Valor2'),
#     ('Chave3', 'Valor3'),
# ]

# Ao invés de utilizar os colchetes, uso as chaves:
# Desta forma, terei um dicionario aqui com X sendo a chave: e o Y o Valor
# d1 = {x: y for x, y in lista}
# print(d1)


""" Mas isso poderia ser Resolvido assim """
# lista = [
#     ('Chave', 'Valor'),
#     ('Chave2', 'Valor2'),
#     ('Chave3', 'Valor3'),
# ]

# d1 = dict(lista)
# print(d1)


""" Podemos fazer Multiplicações também """
# Os valores serão modificados
# lista = [
#     ('Chave', 'Valor'),   #Duplicado
#     ('Chave2', 2),   #Multiplicado
#     ('Chave3', 3),   #Multiplicado
# ]

# d1 = {x: y * 2 for x, y in lista}
# print(d1)


""" Podemos deixar Maiúsculo também """
# lista = [
#     ('Chave', 'Valor'),   #Duplicado
#     ('Chave2', 'Valor 2'),   #Multiplicado
#     ('Chave3', 'Valor 3'),   #Multiplicado
# ]

# Apenas com a função dict, não daria para fazer isto.
# d1 = {x.upper(): y.upper() for x, y in lista}
# print(d1)


""" Com Enumerate e range """
# Elemento X pegou Função Enumerate como Chave e o Valor que é o Y pegou a função range como valor 
# d1 = {x: y for x, y in enumerate(range(5))}
# print(d1)


""" Criando um Set """
# d1 = {x for x in range(5)}
# print(d1, type(d1))


""" Outro exemplo com a Função Range """
# d1 = {f'Chave_{x}': x*2 for x in range(5)}
# print(d1)