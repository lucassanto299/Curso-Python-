""" Funções Def em Python  """
"""---Argumentos e *Args de **Kwargs---"""
# Funciona praticamente como os Desempacotamentos
def func(*args):

    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))

func(1,2,3,4,5)

""" Funcicina Praticamente como listas """
list = [1,2,3,4,5]

n1, n2, *n = list    #Estou pegando os dois primeiros elementos da minha lista e colocando restante em uma nova lista na variavel n, para isso utlizamos * em listas

print(n1, n2, *n)

""" Eu não posso alterar o valor de tuples (deste jeito) """
def func2(*args2):

    args2[0] = 20  # Aqui iria me gerar um erro, pois eu não posso mudar o índice de uma tuple
    print(args2)
    
func2(1,2,3,4,5)

""" Mas Para mudar alterar o valor de uma Tupla, podemos fazer assim """
def func2(*args2):

    args2 = list(args2)   #Convertemos essa Tupla em uma list(utilizando casting), aqui. Pois dessa maneira, posso modificar seu valor.
    args2[0] = 20  
    print(args2)
    
func2(1,2,3,4,5)

""" Se eu não precisar alterar seu Valor, posso trabalhar com ele assim mesmo, da mesma forma que listas """
def func2(*args2):
    
    for v in args2:   #A cada volta do laço ele pega um valor.
        print(v)
    
func2(1,2,3,4,5)

""" Desempacotar uma lista dentro da função print e ainda utilizar um separador entre os valores """
# Aqui eu irei mandar minha lista desempacotada
def func(*args):
    
   print(args)

list = [1,2,3,4,5]       
list2 = [30,40,50,60]    
func(list, '6')    # Se eu adicionar um elemento fora da minha lista ele vai ficar na tupla da função e não fazendo parte da lista 

# """ Para fazer parte da lista """
#Preciso mandar a lista desempacotada, para que ai sim ela faça parte da tupla da função
func(*list, 10,15,20)
func(*list, *list2) # Desta forma acontece o merge das listas, fazendo parte de uma só, que é a da função.

""" Kwargs (Argumentos Com Palavras Chaves/ Argumentos Nomeados) """
def func(*args, **kwargs): 
    
   print(args)
   print(kwargs)    #Apenas desta forma irá parecer meus argumentos nomeados, se não, irá ficar apenas os args
   print(kwargs['nome'], kwargs['sobrenome']) # Tendo acesso a algo especifico. 

list = [1,2,3,4,5]       
list2 = [30,40,50,60]    

func(*list, *list2, nome= 'Lucas', sobrenome = 'Santos')

""" Se eu desejar saber se alguém enviou alguma chave ex: se tem nome, sobrenome ou idade etc..  """
def func(*args, **kwargs): 
    
   idade = kwargs.get('idade')    #kawargs.get: Se existir um argumento nomeado chamado 'idade', ele pega. Get: Significa pega.
   
   if idade is not None:
       print(idade)
   else:
       print('Idade não existe!')

list = [1,2,3,4,5]       
list2 = [30,40,50,60]    

func(*list, *list2, nome= 'Lucas', sobrenome = 'Santos')

""" Se eu souber que meu argumento nomeado existe, eu posso fazer direto """
def func(*args, **kwargs): 
    
    print(args)
    idade = kwargs['idade']   #Fazendo desta forma direta. 
    print(idade)

list = [1,2,3,4,5]       
list2 = [30,40,50,60]    

func(*list, *list2, nome= 'Lucas', sobrenome = 'Santos', idade='27')