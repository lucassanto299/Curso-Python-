# # Operadores Relacionais 

# """ 
# == Igualdade  
# >  Maior que 
# >= Maior que ou igual a 
# <  Menor que
# <= Menor que ou igual a 
# != Diferente
# """
# nome = input('Qual é seu nome: ');
# idade = input('Qual é sua idade: ');

# idade = int(idade) 

# # Limite para pegar empréstimo 
# idade_menor = 20 # Muito jovem 
# idade_maior = 30 # Passou da idade

# if idade >= idade_menor and idade <= idade_maior:
#     print(f'{nome} pode pegar o empréstimo.')
# else: 
#     print(f'{nome} Não pode pegar o empréstimo.')


# Agora iremos ver Operadores Lógicos 
# """ 
# and  E   (Somente se as duas condições forem verdadeira vai dar True)
# or   Ou  (Se uma ao menos uma delas for verdadeira vai dar True)
# not  Não (O operador not não precisa de duas condições/expressões, ele precisa somente de uma.
# Ele é um inversor/inversão, pois o papel dele é inverter o valor)
# in  (Verifica/checar se algo esta dentro da expressão)
# not in (Inverte a expressão: Se isso aqui não estiver dentro, faça tal coisa..)
# """

# a = ''
# if not a: # Utilizamos o not também para emitir um alerta para preencher um campo. 
#     print('Preencha o valor de a.')

# # in 
# nome = 'Lucas Santos'
# if 'u' in nome:
#     print('Existe a letra U no seu nome.')


# # not in 
# if 'sadasdsa' not in nome:
#     print('Não existe')

# # ex
# usuario = input('Nome de Usuário: ')
# senha = input('Senha: ')

# usuario_ls = 'Lucas Santos'
# senha_ls = '123'

# if usuario == usuario_ls and senha == senha_ls:
#     print('Você está logado!')
# else: 
#     print('Senha invalida')

