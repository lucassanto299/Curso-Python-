""" Desafio List Comprehension em Python """

string = '0123456789012345678901234567890123456789'
jump = 10

lista = [string[i:i + jump] for i in range(0, len(string), jump)]
retorno = '.'.join(lista)
print(lista)
print(retorno)


""" Passo a Passo """
# string = '0123456789012345678901234567890123456789'
# jump = 10

# contadores = [i for i in range(0, len(string), jump)] 
# tuplas = [(i, i + jump) for i in range(0, len(string), jump)]
# lista = [string[i:i + jump] for i in range(0, len(string), jump)]
# raw = [f'{i}:{i + jump}' for i in range(0, len(string), jump)]
# retorno = '.'.join(lista)

# print(len(string))
# print(contadores)
# print(tuplas)
# print(raw)
# print(lista)
# print(retorno)