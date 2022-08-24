# Formatando Valores com Modificadores

""" 
:s - Texto (strings)
:d - Inteiros (int)
:f - Números de Ponto Flutuante (float)
:.(número)f - Quantidade de casas decimais (float)
:(caractere) (> ou < ou ^) (quantidade) (tipo - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

from this import d


num = 15
print(f'{num:0>10}') #Aqui estou abrindo meu formatador com : e dizendo que quero o número 0 / > aqui estou referenciando que quero a esquerda / 10 quantos números após eu quero a esquerda contando com que eu já tenho. Portanto serão Nove 0 

print(f'{num:0^10}') #Aqui eu já deixo no centro


num2 = 1150
print(f'{num2:.2f}') #Ele vai ter duas casas decimais com Dois 0

num3 = 1250
print(f'{num3:0>10.2f}') #Combinei os valores agora. Adicionei os 0 a equerda e com duas casas decimais 


nome = 'Santos'
print(len('####################'))

print(f'{nome:#^46}') #Aqui estou colocando meu nome no centro e preenchendo com # 50 vezes o restante dos espaços


Usando a Função format

nome = 'Lucas Santos'
nomeCompleto = '{:#>50}'.format (nome) #Utilizamos as chaves para representar a nossa variavel/ Se eu quiser modificar minha variavel, eu coloco : dentro de chaves/ e quero preencher meu nome com @ / do lado esquerdo do meu nome/ com 50 caracter
print(nomeCompleto)


# Utilizando agora com Variáveis Nomeadas
nome = 'Lucas Santos'
nomeCompleto = '{n:0<50}'.format(n=nome) #Se eu quiser chamar minha variável nome de n agora, eu posso. e estou falando para colocar 0 Cinquentavezes a Direita
print(nomeCompleto)

# Agora com indices /Chamando pelo indice

nome = 'Lucas'
sobrenome = 'Santos'

nomeFormatado = '{0:$^50} {1:#^50}'.format(nome,sobrenome) # Aqui eu chamei por indices e modifiquei cada um 

print(nomeFormatado)


# Outras funções
nome = 'Lucas Santos'
print(nome.lower())  # Tudo Minusculo
print(nome.upper())  # Tudo Maiusculo
print(nome.title())  # Primeiras Letras Maiusculas 