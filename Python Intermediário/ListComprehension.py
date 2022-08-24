""" List Comprehension in Python (Compreensão de Listas) """

""" 
- Otimização (Performace do Código)
- Escrever menos Linha de Código
"""

""" Iterar sobre uma List com 1 Linha de Código """
l1 = [1,2,3,4,5,6,7,8,9]
l2 = [value for value in l1]
print(l2)

""" Ex 2 Multiplicando Iteraveis """
l1 = [1,2,3,4,5,6,7,8,9]
l2 = [value * 2 for value in l1]
print(l2)

""" Ex 3 Usando Dois For com uma Tupla"""
l1 = [1,2,3,4,5,6,7,8,9]
l2 = [(value, value2) for value in l1 for value2 in range(3)]
print(l2)

""" Ex 4 Invertendo valores Strings """
l1 = ['Lucas', 'Santos', 'Dev']
l2 = [value.replace('s', '*') for value in l1]
print(l2)

""" Alterando a Tipagem e Trocando os Valor de uma Tupla """
tupla = (
        ('chave', 'valor'),
        ('chave2', 'valor2'),
)

inverse = [(y, x) for x, y in tupla]
print(inverse)

inverse = dict(inverse)
print(inverse)

print(inverse['valor2'])

""" Filtrando uma List For e Dois IF """
l1 = list(range(100))
filtro = [value for value in l1 if value % 2 == 0 if value % 8 == 0]
print(filtro)

""" Utilizando o Else """
l1 = list(range(100))
filtro_Else = [value if  value % 3 == 0 and value % 8 == 0 else 'Não é divisível' for value in l1]
print(filtro_Else)
