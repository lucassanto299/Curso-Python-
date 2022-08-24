""" Criando Escrevendo Apagando Arquivos em Python """

""" 
Isso é bem importante porque:
- Se você tiver um sistema que tenha configurações - Você pode salvar essas configurações em um dicionário
- Converter isso para json, salvar no arquivo. Depois quando você precisar, pode puxar esses dados Json do arquivo
- E depois converter de volta em um dicionário e utilizar em seu sistema
"""

""" Modo mais Básico de Falar/Trabalhar com isso """
""" Criando um arquivo txt """
# file = open('abc.txt','w+')  #Eu falei aqui que eu quero abrir um arquivo para escrita, mas quando eu coloquei o W+: Estou dizendo que eu quero Leitura e Escrita
#                              #Portanto eu posso ler e escrever neste arquvio W+

# #Escrevendo coisas dentro do meu arquivo:
# file.write('Linha 1 \n')
# file.write('Linha 2 \n')
# file.write('Linha 3 \n')

# #Se eu quiser Ler este arquivo (Existe várias funções em python para fazer isto):
# file.seek(0, 0)  #Seek(procura) Move o curso de volta para o topo do arquivo. E aqui eu passo dois parâmetros: A posição e A relatividade de onde você esta procurando
#                  #Geralemnte se usa 0 mesmo, pois queremos buscar a posição absoluta do arquivo. se eu desejar começar de 2 caracter para frente, coloco um 2 na frente (Começa no Top do arquivo e vai descendo)

# print('Lendo linhas:')
# print(file.read())  #Ele vai ler o arquivo inteiro e me retornar uma string
# print('#'* 30)
# # E tenho que voltar o cursor para o topo novamente
# file.seek(0, 0)

# """ Se eu quiser ler Linha por linha """
# print(file.readline())  #Lendo a primeira linha
# print(file.readline())  #Agora ele vai ler a segunda linha também
# print('#'* 30)
# file.seek(0, 0)

# #Posso jogar linha por linha em uma Lista
# # print(file.readlines()) # pode ser usado um for também
# #ou
# for linha in file.readlines():
#     print(linha, end='')   #end para tirar a quebra de linha

# #Assim que eu terminar de trabalhar no arquivo, eu preciso o fechar, para não gerar problemas.
# file.close()

""" Outra Forma, utilizando blocos (Try e Except) utilizado para abrir arquivos também """
# Vamos abrir o arquivo com bloco try
# try:
#     file = open('abc.txt', 'w+')
#     file.write('Linha 1')
#     file.seek(0, 0)
#     print(file.read())
# finally:   #Utilizamos o Finally, mesmo que aconteça algum erro antes do fanally, ele fechará o arquivo
#     file.close()

""" Melhor Maneira de se Trabalhar com Abertura de Arquivos em Python """
"""             Gerenciadores de Contexto                             """

# with open('abc.txt', 'w+') as file:   #Esse gerenciador de arquivo, assim que ele terminar de executar, ele já fecha o arquivo para mim.
#     file.write('Linha 1\n')
#     file.write('Linha 2\n')
#     file.write('Linha 3\n')

#     file.seek(0)
#     print(file.read())

""" Se eu desejar apenas Ler um arquivo """
# with open('abc.txt', 'r') as file:   #utilizando r: Só para leitura
#     print(file.read())


""" Adicinando coisas no Arquivo sem Apagar """
# with open('abc.txt', 'a+') as file:   #Cada vez que eu executar com a+, ele vai criando uma nova linha
#     file.write('Outra linha \n')
#     file.seek(0)
#     print(file.read())

""" Se eu desejar apagar o arquivo txt """
# import os 
# os.remove('abc.txt')


""" Importando Módulo Json """
#JSON é uma sintaxe para armazenar e trocar dados.
#JSON é texto, escrito com notação de objeto JavaScript.
#Python tem um pacote embutido chamado json, que pode ser usado para trabalhar com dados JSON

import json
#Criando um Dicionário 

d1 = {
    'Pessoa 1': {
        'Name': 'Lucas',
        'Last Name': 'Santos',
        'Ages': '27',
    },
    'Pessoa 2': {
        'Name': 'Amira',
        'Last Name': 'Ahmad',
        'Ages': '29',
    },
}

#Convertendo este dicionário para json 
# json.dumps(), converte para uma string Json 
d1_jason = json.dumps(d1, indent=True)   #Usei o indent(True), para ficar melhor a visualização

#Jogando dentro de um arquivo 
with open('abc.json', 'w+') as file:   # W+ porque eu quero que ele apague o arquivo se este já existir e jogue esse dicionário lá dentro novamente
    file.write(d1_jason)    #E agora meu arquivo.json foi criado

""" Agora vamos criar um novo arquivo para ler json """