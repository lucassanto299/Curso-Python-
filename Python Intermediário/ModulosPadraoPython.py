""" Módulos padrão do Python """
# """ 
# - Módulos são arquivos .py (Que Contém código Python) que você pode importar, e servem para expandir
# as funcionalidades padrão da linguam.

# - Resumo: 
# Se você precisar adicionar qualquer outra funcionalidade fora a padrão
# dentro da linguagem, você pode:

# - Instalar Módulos Externos
# ou
# -Importar Módulos que já vem com a linguagem
# """

""" Ex: Saber qual plataforma o Python esta sendo utilizado neste momento """
#importando Módulo Sys
# import sys  #Desta forma, eu acesso tudo que o Módulo sys fornece
# print(sys.platform)  #Estou pedindo para o Python acessar o Módulo Sys e acessar esse platform/ no caso irá aparecer minha plataforma, Windows

""" Já desta maneira, eu seleciono o que eu desejo acessar do Módulo """
# from sys import platform
# print(platform)   #E ai eu chamo desta forma, pois já selecionei esta opção específica

""" Posso dar um Apelido também para meu platform, como se estivesse jogando seu valor dentro de uma variável """
# from sys import platform as sistema
# print(sistema)   #Ai só chamo pela minha variável


""" Se eu desejar gerar números aleatórios tem o (Módulo Random)"""
# import random 
# for value in range(10):  #A cada vez que gerar um número aleatorio, irá passar pelo meu for em um range 10 vezes, ou seja, vai se repetir dez 
#     print(random.randint(0,10))  #Do número aleatorio. eu quero randint: número aleatório inteiro (entre 0 e 10) 

""" Se eu desejar importar de forma específica """
# from random import randint 
# for value in range(10):
#     print(randint(0,10))  #Agora posso utilizar direto a função randint()


""" Cuidado Para Não sobre escrever uma função, quando o Módulo da função Já estiver específico """
# Ex:
# from random import randint  #Eu importei o Módulo randint

# def randint(*args):   #E neste momento eu acabei o sobrescrevendo  -> randint. Portanto, quanto eu o chamar, vai chamar minha função com seu processamento ao invés de chamar o Módulo, pois esta com mesmo nome
#     return 'hahaha'                                                #-> Portanto neste caso, basta renomear a função com outro nome, para não dar conflito com o nome do Módulo importado ou simplesmnete dando um
#                                                                    #-> Apelido para ela ou seja, jogar em uma variável: from random import randint as QualquerNome
# for value in range(10):
#     print(randint(0,10))  #Agora posso utilizar direto a função randint()


""" Outra Maneira: Importar tudo de um Módulo (from random import *) """
#Estou dizendo para importar Tudo do Módulo random 
#A chance de eu sobrescrever algo do Módulo, é grande. E se eu precisar usar algo que eu sobrescrevi algo de dentro do módulo random, para debugar isso fica complicado.
#Se eu utilizar somente random(), vai me gerar um número aleatório entre 0 e 1
# from random import *

# for value in range(10):
#     print(randint(0,10))  #Fica difícil de eu saber desta maneira (Importando tudo do Módulo) de eu saber que esta vindo deste módulo específico

""" Se um Módulo ou Pacote não estiver presente, podemos utilizar a Ferramenta PIP para instalar o que eu desejar """
import pymysql   #Basta instalar no terminar pip install e o Módulo/Pacote que eu quero instalar
                 #Se eu desejar remover: pip uninstall pymysql