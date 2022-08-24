""" Funções Decoradoras e Decoradores em Python """
""" 
As Funções Decoradoras: Irão envolver as funções que você quiser, mudando ou não o comportamento delas se você preferir.
A função decorador: É utilizada para adicionar algum recurso na função. 
Ex: O tempo que uma função leva para executar
Ex2: Podemos criar arquivos de log, toda vez que uma função for executada, geramos um log.
"""
""" Vamos Passo a Passo """
#Definindo uma função básica:
# def fala_oi():
#     print('Oi!')

# fala_oi()

#Sabendo disto, eu sei também que posso jogar uma função em uma variável
# def fala_oi():
#    return print('Oi!')

# saudacao = fala_oi #Só que sem executar a função: fala_oi sem os Parenteses ()
# saudacao()  #Seria a mesma coisa que chamar a função fala_oi(), mas agora minha variável, é esta função também. 


#Função dentro de Função
#Criei a função master, dentro do corpo da função master, criei outra função para fazer algo que eu queira
# def master():
#     def slave():   #Estpi criando outra função dentro da mater
#         print('Oi!')   #Que imprime algo na tela.
#     slave()   #Tenho que chamar ela aqui dentro, para ela poder ser executada.

# master()  #Então a master, esta criando uma função, que vai fazer alguma coisa e ai ela executa está função dentro do corpo dela mesmo.

""" Só que desta Maneira, eu também posso retornar ela """
# def master():
#     def slave():   
#         print('Oi!')   
#     return slave   #retornando o valor do slave, sem executar

# variavel = master()  #Tornando possivel eu jogar dentro de uma variável assim. Ou seja, estou pegando minha variável e dizendo que ela é igual a master, só que a master cria uma função e retorna esta função sem executar
# variavel()


""" De forma completa """
# def master(funcao):   #Criei uma função chamada de master, que recebe como parâmetro uma função
#     def slave():    #Dentro da função master, estou definindo uma função slave(uma função escreva da master)
#         print('Agora está decorada.')
#         funcao()    #Que esta fazendo o trabalho de executar a função master, que esta recebendo uma outra função
#     return slave    # Retorna o valor da slave sem executar ela

# def fala_oi():
#     print('Oi')   #Esse oi, está vindo dessa função que estou passando como parâmetro para master e a slave está executando ela dentro.

# # variavel = master(fala_oi)
# # variavel()
# # OU
# fala_oi = master(fala_oi)  # e agora isso é uma função Decorada em Python

# fala_oi()


""" Função Decorada e Decorador (Completo)"""
# Essa esta sendo minha função decoradora
# def master(funcao):  
#     def slave():    
#         print('Agora está decorada.')
#         funcao()    
#     return slave    
# @master   #E agora eu tenho um decorador ou seja, esta função esta decorada com o decorador master
# def fala_oi():
#     print('Oi')   

# fala_oi()


""" Função Decorada e Decorador com Args e **Kwargs """
# def master(funcao):  
#     def slave(*args, **kwargs):    #Agora ela vai poder receber parâmetros
#         print('Agora está decorada.')
#         funcao(*args, **kwargs)    #Agora ela repassa para nossa função da master
#     return slave    
# @master  
# def fala_oi():
#     print('Oi')   

# @master  #Vai gerar um erro eu passando o decorador, pois tem um argumento Nomeado
# def outra_funcao(msg):
#     print(msg)

# outra_funcao('Lucas Santos')


""" Ex: O tempo que uma função leva para executar """
# from time import time  #Só para vermos o tempo!
# from time import sleep #Fazer alguma função dormir por um tempo

# def velocidade(funcao):  #Vai receber outra função, pois ela uma função decoradora
#     def interna(*args, **kwargs):  #Essa função interna vai receber args e kwargs 
#         start_time = time()  #Tempo de inicio, que neste caso será o tempo atual
#         resultado = funcao(*args, **kwargs)    # E vai executar e retornar a funcao
#         end_time = time()   #Para pegar o tempo depois que ela executou
#         tempo = (end_time - start_time) * 1000 #Se não, me retornaria um número gigante, por isso estou pegando Milissegundos
#         print(f'A função {funcao.__name__}, levou {tempo:.2f}ms para executar.')
#         return resultado
#     return interna     #E a função velocidade vai retornar a função interna sem executar


# @velocidade   #E aqui estou decorando essa função com meu decorador Velocidade
# def demora(): 
#     for value in range(5):
#         print(value)
#         sleep(1)  #A cada volta do laço ela vai demorar 1 segundo, total de 5 segundos pela função range