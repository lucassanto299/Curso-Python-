# Formantando valor/ Modificadores
# Posso fazer desta maneira para números:

# from this import d 

# num = 15
# print(f'{num:#^20.2f}')

# nome = 'Lucas Santos'
# print(f'{nome:*^20}')

# Jogando isso a uma variável agora
# nome = 'Lucas Santos';
# nomemod = '{:*^20}'.format(nome)
# print(nomemod)

# Com variáveis Nomeadas
# nome = 'Lucas Santos'; 
# nomemod = '{n:*^20}'.format (n=nome)
# print(nomemod)


# nome = 'Lucas Santos';
# caracterNome = len(nome);
# acc = 0
# while caracterNome > acc:
#     letra = nome[acc] 
#     if letra == 'a':
#         letra = 'A'
#         seila = '123' #
#     acc +=1
#     print(letra, seila, end='')

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



""" Validar CPF (Algoritmo de Cálculo para Validar um CPF) """
""" CPF = 168.995.350-09 
Para obter o Primeiro digito, após o traço do cpf, fizemos o primeiro cálculo que é multiplicar as 9 primeiras casas do cpf
---------------------------
1 * 10 = 10     #   1 * 11 = 11 <-
6 * 9  = 54     #   6 * 10 = 60
8 * 8  = 64     #   8 * 9  = 72
9 * 7  = 63     #   9 * 8  = 72
9 * 6  = 54     #   9 * 7  = 63
5 * 5  = 25     #   5 * 6  = 30
3 * 4  = 12     #   3 * 5  = 15
5 * 3  = 15     #   5 * 4  = 20
0 * 2  = 0      #   0 * 3  = 0
     297        # ->0 * 2  = 0

11 - (297 % 11) = 11    #   11 - (343 % 11) = 9 
11 > 9 = 0              #
Digito 1 = 0 11         #   Digito 2 = 9
"""


""" Minha Solução em Desenvolvimento """
# cpf = '168.995.350-90'
# cpfmod = cpf[:11]

# for number, letra in enumerate(cpfmod):
#     if letra == '.' or letra == '-':
#         letra = ''
#         letra = len(letra)
#     print(number, letra)


""" --------------------------------- """
""" Agora utilizando For para resolver esse problema """
""" Como um Sênior faria """
# while True:
#     # cpf = '16899535009'
#     cpf = input('Digite um CPF: ')
#     novo_cpf = cpf[:-2]                 # Elimina os dois últimos digitos do CPF
#     reverso = 10                        # Contador reverso
#     total = 0

#     # Loop do CPF
#     for index in range(19):
#         if index > 8:                   # Primeiro índice vai de 0 a 9,
#             index -= 9                  # São os 9 primeiros digitos do CPF

#         total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

#         reverso -= 1                    # Decrementa o contador reverso
#         if reverso < 2:
#             reverso = 11
#             d = 11 - (total % 11)

#             if d > 9:                   # Se o digito for > que 9 o valor é 0
#                 d = 0
#             total = 0                   # Zera o total
#             novo_cpf += str(d)          # Concatena o digito gerado no novo cpf

#     # Evita sequencias. Ex.: 11111111111, 00000000000...
#     sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

#     # Descobri que sequências avaliavam como verdadeiro, então também
#     # adicionei essa checagem aqui
#     if cpf == novo_cpf and not sequencia:
#         print('Válido')
#     else:
#         print('Inválido')

""" Nova Forma, fazendo um gerador de cpf """
from random import randint    #Gerar um número aleatório
numero = str(randint(100000000, 999999999))    #Aqui iremos ter um número aleatório entre 1000000 e 99999999/ str porque vou ter que converter para uma string, pois irei receber uma string no input


novo_cpf = numero                 # Elimina os dois últimos digitos do CPF
reverso = 10                        # Contador reverso
total = 0

# Loop do CPF
for index in range(19):
     if index > 8:                   # Primeiro índice vai de 0 a 9,
          index -= 9                  # São os 9 primeiros digitos do CPF

     total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

     reverso -= 1                    # Decrementa o contador reverso
     if reverso < 2:
          reverso = 11
          d = 11 - (total % 11)

          if d > 9:                   # Se o digito for > que 9 o valor é 0
               d = 0
          total = 0                   # Zera o total
          novo_cpf += str(d)          # Concatena o digito gerado no novo cpf

print(novo_cpf)