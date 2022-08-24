
""" For e Else """

variavel = ['Santos', 'Amira', 'Lineu']

for nomes in variavel:
    if nomes.startswith('S'):
        print('Começa com "S"', nomes)
    else:
        print('Não começa com "S"', nomes)


# Outra forma
variavel = ['Santos', 'Amira', 'Lineu', 'Matheus']
valor_falso = False

for nomes in variavel:
    if nomes.lower().startswith('s'):
        valor_falso = True

if valor_falso:
    print('Existe uma palavra que começa com "S"')
else: 
    print('Não existe uma palavra que comece com "S"')


# Mais simplificado Ainda 
variavel = ['Santos', 'Amira', 'Lineu']

for nomes in variavel:
    if nomes.lower().startswith('s'):
        print('Existe uma Palavra que começa com a letra "s"')
        break
else:
    print('Não existe uma palavra que comece com a letra "s"')