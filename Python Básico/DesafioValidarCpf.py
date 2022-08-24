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
cpf = '168.995.350-90'
cpfmod = cpf[:11]

for number, letra in enumerate(cpfmod):
    if letra == '.' or letra == '-':
        letra = ''
        letra = len(letra)
    print(number, letra)


""" Solução 'Correta!'"""
cpf = '16899535090'
new_cpf = cpf[:-2]    #Aqui cpf[:-2] Estou tirando os últimos dois dígitos 
reverso = 10
total = 0
while True:
    for index in range(19):
        if index > 8:
            index -=9   
        
        total += int(new_cpf[index]) * reverso                        #print(cpf[index],index,reverso)
        
        reverso -= 1
        if reverso < 2:
            reverso = 11
        digito = 11 - (total % 11)

        if digito > 9:
            digito = 0
            total = 0
            new_cpf += str(digito)

    if cpf == new_cpf:
        print('Válido')
    else:
        print('Inválido')
           

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

