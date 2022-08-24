# Método sep='' e end=''
# print('Hoje', 'esta', 'sendo', 'muito', 'bom', sep='-', end='!')
# print('Porque', 'eu', 'finalmente', 'estou', 'vendo', 'os', 'frutos', 'das', 'minhas', 'escolhas', 'até', 'aqui', end='.')

# Função type
# inteiro = 10
# ponto_flutante = 10.5
# resto = 10 * 5
# potencia = 2 ** 3 
# boleano = 10 == 10 
# texto = 'Olá!'

# print(type(inteiro)); 
# print(type(ponto_flutante));
# print(type(resto));
# print(type(potencia));
# print(type(boleano));
# print(type(texto));

# Métodos Math
# import math
# cima = 10.5
# baixo = 10.6
# passa_positivo = -3
# MetadeCima = 4.6
# MetadeBaixo = 4.4
# print(math.ceil(cima));
# print(math.floor(baixo));
# print(math.abs(passa_positivo));
# print(round(MetadeCima));
# print(round(MetadeBaixo));
# print(math.pow(2,3));

# Função len
# nome = 'Lucas Santos';
# caracteres = len(nome);
# print(caracteres);

# Place Holders 
# """ Pass """
# valor = True
# if valor: 
#     pass
# else:
#     print('Não vai executar o print');

# """ Ellipsis """
# valor2 = True
# if valor2:
#     ...
# else:
#     print('Vai aparecer?')

# .isdigite()
# dado = input('Digite um número inteiro: ')
# if not dado.isdigit():
#     print('Você não digitou um inteiro!')
# else:
#     print('É um número inteiro');

# ex2
# num = input('Digite um número: ')
# if not num.isdigit():
#     print('Você tem que digitar um número!')
# elif num:
#     num = int(num)
#     if num % 2 == 0:
#         print(f'{num}, é par!')
#     else:
#         print(f'{num}, é impar');

# In(existe/contém)
# nome = input('Digite seu nome: ')
# letra = input('Digite uma letra: ')

# if letra in nome:
#     print(f'Existe a letra: {letra}, em seu nome!')
# else: 
#     print(f'Não existe a letra: {letra}, em seu nome!')

# Not in 
# nome = input('Digite seu nome: ')
# letra = input('Digite uma letra: ')

# if letra not in nome:
#     print('Essa letra não contém no seu nome!')

# Formatando Valores com Modificadores: 
# from this import d
# num = 15

# print(f'{num:0>10}');
# print(f'{num:0^10}');

# num2 = 1150

# print(f'{num:.2f}')

# num3 = 1250

# print(f'{num:0>10.2f}')

# nome = 'Santos'

# print(f'{nome:#^50}')

""" Ou .format """
# nome = 'Lucas Santos'
# nomemod = '{:#^50}'.format (nome)

# print(nome)
# print(nomemod);

""" Com Variáveis Nomeadas """
# nome = 'Lucas Santos'
# nomemod = '{n:*^20}'.format(n=nome)

# print(nome)
# print(nomemod)

""" Outras Funções """
# nome = 'Lucas Santos'
# print(nome.lower());
# print(nome.upper());
# print(nome.title());


""" Chamando Pelo Indice """
# nome = 'Lucas'
# sobreNome = 'Santos'

# nomemod = '{0:$^20} {1:#^20}'.format(nome,sobreNome)


# print(nomemod)
""" Manipulando Strings """
# texto = 'Python s2'
# print(texto[0:7:2])  #Step 
# print(texto[:7])
# print(texto[7:])
# print(texto[-2])

# While True
# while True:
#     nome = input('Qual é seu nome: ')
#     print(f'Olá, {nome}!')

""" Com Contador """
# acc = 0
# while acc < 5:
#     print(acc)
#     acc += 1 

""" Utilizando Continue """
# acc = 0
# while acc < 5:
#     continue    
    
#     print(acc)
#     acc +=1
# print('Let`s Go!')

# acc = 0 
# while acc < 10:
#     if acc == 3:
#         print(acc)
#         continue
#     print(acc)
#     acc +=1 

# print('Let`s Go!')

# contador = 1
# acumulador = 1
 
# while contador <= 10:
#     print(contador, acumulador)
   
#     if contador > 5:
#         break
#     acumulador = acumulador + contador
#     contador += 1
 
 
# print('Sai fora!')
# contador = 1
# acumulador = 1
# while contador <= 10:
#     print(contador, acumulador)
   
#     if contador > 5:
#         break
#     acumulador = acumulador + contador
#     contador += 1
# else:
#     print('Sai fora!')


# Interando Strings com While em Python 
# nome = 'Lucas Santos'
# stringtotal = len(nome)
# acc = 0
# while stringtotal > acc:
#     print(nome[acc], acc)
#     acc +=1    

""" Passando para Maiúsculo a Letra A """
# nome = 'Lucas Santos';
# caracterNome = len(nome);
# acc = 0
# while caracterNome > acc:
#     letra = nome[acc] 
#     if letra == 'a':
#         letra = 'A'
#     acc +=1
#     print(letra, end='')

""" Perguntando para o Usuário qual Letra em M """
# frase = 'Let`s go! cada um tem seu tempo, faça o seu! '
# print(frase)
# letra = input('Qual letra da frase Você deseja que seja maiúscula: ')
# tamanho_frase = len(frase)
# acc = 0

# while acc < tamanho_frase:
#     novaString = frase[acc]
#     if novaString == letra:
#         novaString = letra.upper()
#     acc +=1
#     print(novaString, end='')

# For In
""" Com while ficaria assim """
# texto = 'Python';
# acc = 0;

# while acc < len(texto):
#     print(texto[acc], acc)
#     acc +=1

""" Agora com For In """
# texto = 'Python'
# for letra in texto: 
#     print(letra)

""" Com enumerate """
# texto = 'Python'
# for n, letra in enumerate(texto):
#     print(n,letra);

""" Utilizando a Função Range() """
# for numero in range(10):
#     print(numero)

""" Modificando os Parâmetros da Função Range() """
# for numero in range(20,10,-1):
#     print(numero)

""" Sabendo os Multiplos """
# for multiplo in range(0,100,8):
#     print(multiplo)

""" Podemos Fazer Assim também """
# for multiplo in range(100):
#     if multiplo % 8 == 0:
#         print(multiplo)

""" Interando For In com Strings """
# texto = 'Python'
# novaString = ''

# for letra in texto:
#     if letra == 't':
#         novaString += letra.upper()
    
#     elif letra == 'h':
#         novaString += letra.upper() 
#     else:
#         novaString += letra
# print(novaString)




