""" Colocando em Prática Funções """
# def greet():
    
#     print('Hello!')

# greet()

""" Com Parâmetro """
# def nome(name):    #Criei meu Parâmetro
    
#     print(name)    #Estou dizendo o que é para fazer com meu argumento.

# nome('Lucas Santos')    #Estou chamando minha Função e passando meu argumento para o Parâmetro 

""" Para além de 1 Parâmetro """
# def greetname(greet,name):
   
#     print(greet,name)

# greetname('Olá', 'Lucas Santos')

""" Colocando Valor Padrão  """
# def massege(greet='Olá', name='Lucas Santos'):

#     print(greet, name)

# massege()
# massege('Olá', 'Fulano')

""" Alterando Ordem e Valor Padrão """
# def phrase(ends='The ends',means='justify the means'):
  
#     print(ends, means)

# phrase()
# phrase(means='Os Meios justificam', ends='O fim?')

""" .Replace Trocando De lugar/trocando valor, os elementos ou Caracters de Algo """

"""---- Atribuindo o mesmo Valor de um Parâmetro ----"""
# def phrase2(day, night):
#     day = day.replace(day, night)         #O Valor do day, foi substituido pelo Night, ou seja, day tem valor de night agora
#     night = night.replace(night, day)     #Sendo assim, o night neste caso esta com o valor do day que é Noite!
#     print(day, night)                     

# phrase2('Bom dia!', 'Boa noite!')

# """ Trocando Apenas Se Receber a Mesma Phrase  """
# def phrase2(day, night):
#     day = day.replace('Bom dia!', 'Boa noite!')         #Estou dizendo que o primeiro valor de day, irá ser trocado pelo Boa noite
#     night = night.replace('Boa noite!', 'Bom dia!')     #O valor do Night, irá ser Bom dia
#     print(day, night)                     

# phrase2('Bom dia!', 'Boa noite!')     

# """ Não importa o Valor que eu Atribuir ao meu Parâmetro """
# def phrase2(day, night):
#     day = day.replace(day, 'Boa noite!')        #Por conta disto, estou dizendo para trocar este valor que ele receber, por outro!
#     night = night.replace(night, 'Bom dia!')    #Por conta disto, estou dizendo para trocar este valor que ele receber, por outro!
#     print(day, night)                     

# phrase2('qualquer coisa!', 'sei lá')

""" Função que Retorna Algum Valor """
"""--- Vai Me Retornar um Valor Padrão, ao menos que eu Modifique ---"""
# def attendance(call='Pode vir Sr',user='Usuário'):
    
#     return f'{call} ,{user}' 

# result = attendance()
# print(result)

""" Função Return """
# """--- Para o Print fora da Função ter um Valor, eu preciso dizer Para Função me retornar o Valor do Parâmetro  ---"""
# def funcao (var):

#     print(var)
   
# variavel = funcao('O valor que eu quero')    #Aqui minha variável irá receber um tipo de dado chamado None: Que signica que não tem valor

# print(variavel)                            #Pois o valor esta isolado dentor da minha função, não tendo como passarp para a variável

""" Agora Return Valor Da função """
# def funcao(value):

#     return value

# phrase = funcao('Vai funcionar')
# print(phrase)

# if phrase:
#     print('Deu certo! ')
# else:
#     print('Não tem Valor')

""" Função que faz divisão """
# def div(value, value2):
    
#     return value / value2

# result = int(div(15,5))
# print(result)

""" Só Para Mostrar que Pode usar 2 Return """
"""--- Pois qualquer Um Vai Cair na Condição ---"""
# def div(value, value2):
    
#     if value2 == 0:
#         return
    
#     return value / value2

# result = div(15,5)
# if result:
#     print('Resultado Aprovado!')
# else:
#     print('Conta Inválida!')

""" Escopo Global """
""" Qualquer um pode pegar o que esta fora do escopo """
# value = 'Algum valor'

# def result():

#     print(value)

# result() 

""" Escopo Local """
""" O que estiver dentro não consigo puxar """
# def value():
    
#     resultado = 'Agum Valor' 
#     print(resultado)

# value()
# print(resultado) #Errrooooo

""" Modificar Escopo Global """
"""--- Tenho que Referênciar que é Global ---"""
""" Detalhe: Não faça isso! """
# phrase = 'Qualquer Coisa'

# def result():
#     global phrase           #Sem referência, estou apenas criando outra variável
#     phrase = 'Outro valor'
#     print(phrase)

# result()
# print(phrase)

""" Forma Correta se Precisar Trabalhar or Modificar uma Variavel Global """
# value = 'Qualquer coisa'

# def func(arg=None):
    
#     arg = arg.replace(arg, 'Trocou!')
#     return arg

# result = func(arg = value)
# print(result)    #Peguei o valor da variavel e modifquei
# print(value)     #Sem alterar a variavel global, mas mesmo assim pegando seu valor e Modf.

""" Passando o Valor de Uma Função para Outra """
# def func(value):
 
#     return value

# seiLa = func('Lucas Santos')

# def func2 (arg):
#     print(arg)

# func2(seiLa)
# """ Or """
# def func():
 
#     value = 'Lucas Santos'
#     return value

# def func2 (arg):
#     print(arg)

# value2 = func()
# func2(value2)

""" Args e Kwargs """
# def func(*args):

#     print(args)
#     print(args[0])
#     print(args[-2])
#     print(len(args))

# func(1,2,3,4,5)

""" Funciona como List """
# list = [1,2,3,4,5]

# n1, n2, *n = list

# print(n1, n2, *n)    #Se eu desejar uma nova lista com restante dos valores, só tiro o * na saída. 

""" Não pode Alterar o Valor de Tuples """
# def func(*args):

#     args[0] = 20
#     print(args)

# func(1,2,3,4,5)

""" Mas posso Alterar o Valor de Um Tuplas/Args Assim """
# def func2(*args):

#     result = list(args)
#     result[0] = 20
#     print(result)

# func2(1,2,3,4,5)

""" Posso Trabalhar com Args também """
# def func(*args):

#     for value in args:
#         print(value)

# func(1,2,3,4,5)

""" Desempacotar uma Lista Dentro de uma Função """
# def func(*args):

#     print(args)

# list = [1,2,3,4,5]
# list2 = [10,20,30,40,50]

# func(list, 3)   # Se eu adicionar um elemento fora da minha lista ele vai ficar na tupla da função e não fazendo parte da lista

""" Para um Elemento fazer parte da Lista Desempacotada """
# func(*list, 3)
# func(*list, *list2)

""" **Kwargs Argumentos Com Palavras Chaves """
# def func(*args, **kwargs):

#     print(args)
#     print(kwargs)
#     print(kwargs['nome'], kwargs['sobrenome'])

# list = [1,2,3,4,5]
# list2 = [10,20,30,40,50]

# func(*list, *list2, nome = 'Lucas', sobrenome = 'Santos')

""" Se eu desejar saber da Existência Kwarg Especifica """
# def func(*args, **kwargs):

#     idade = kwargs.get('idade')
#     if idade is not None:
#         print(idade)
#     else:
#         print('Não existe Idade')

# list = [1,2,3,4,5]
# list2 = [10,20,30,40,50]

# func(*list, *list2, nome = 'Lucas', sobrenome = 'Santos')

""" Se eu desejar Pegar um Kwarg Específico """
# def seila(*args, **kwargs):

#     print(args)
#     idade = kwargs['idade']
#     print(idade)

# list = [1,2,3,4,5]
# list2 = [10,20,30,40,50]

# seila(*list, *list2, nome = 'Lucas', sobrenome = 'Santos', idade = '27')

""" Desafio Funções """
""" 1 """
# def func(saudacao, nome):

#     print(saudacao, nome)

# func('Olá', 'Lucas Santos')

""" 2 """
# def resultado(value1, value2, value3):

#     print(value1 + value2 + value3) 

# resultado(2,2,2)

""" 3 """
# def result(value,percentual):

#     print(value + (value * percentual / 100))

# result(100,10)

""" 4 """
# def fizz_buzz(value):

#     if value % 5 == 0 and value % 3 == 0:

#        return print(value, 'FizzBuzz')
    
#     if value % 5 == 0:

#       return  print(value, 'Buzz')
    
#     if value % 3 == 0:

#        return print(value, 'Fizz')
    
#     else:
#         print(value)

# from random import randint
# for i in range(10):
#     aleatorio = randint(0,100)
#     print(fizz_buzz(aleatorio))

""" Desafio 2 Funções """
""" 1 Crie uma função1 que recebe uma função2 como Parâmetro e Retorne o Valor da função2 executada. """
# def func(arg):
    
#    return arg


# def func2():

#     return print('Lucas Santos')

# func(func2())

""" 2 Crie uma função1 que Recebe uma função2 como Parâmetro e Retorne o Valor da função2 executada. 
Faça a função1 executar duas funções que recebam um número diferente de argumentos. """
# def mestre(funcao, *args, **kwargs):

#     return funcao(*args, *kwargs)

# def name(nome):

#     return f'{nome}'

# def saudar_name(saudacao, nome):

#     return f'{saudacao} {nome}'

# result = mestre(name, 'Lucas Santos')
# result2 = mestre(saudar_name, 'Olá', 'Lucas Santos')

# print(result)
# print(result2)


""" Dicionário """
# questions = {
#     'Question 1': {
#         'Question': 'Quanto é 2 + 2',
#         'answers': {
#             'a': '6',
#             'b': '10',
#             'c': '4',
#         },
#         'answer_secrete': 'c',

#     },
#     'Question 2': {
#         'Question': 'Quanto é 2 * 3',
#         'answers': {
#             'a': '6',
#             'b': '8',
#             'c': '16',
#         },
#         'answer_secrete': 'a',

#     },

# }
# answers_correct = 0
# for question_key, question_value in questions.items():
#     print(f'{question_key}: {question_value["Question"]}')
#     print('Respostas:')
    
#     for answers_key, answers_value in question_value['answers'].items():
#         print(f'[{answers_key}]: {answers_value} ')

#     usuario = input('Sua resposta: ')
    
#     if usuario == question_value['answer_secrete']:
#         print('Parabéns!! Você acertou o/')
#         answers_correct += 1
#     else:
#         print('Eitah, você errou :/')
    
#     print()

# amounth_questions = len(questions)
# percentage = answers_correct / amounth_questions * 100

# print(f'Você acertou {answers_correct} respostas!')
# print(f'Sua porcentagem de acerto foi {percentage}%')




""" Programa que vai executar listar,add, refazer e desfazer tarefas """
# def show_op(todo_list):
#     print()
#     print('Tarefas: ')
#     print(todo_list)

# def todo_undo(todo_list, redo_list):
#     if not todo_list:
#         print('Não tem nada para desfazer')
#         return
#     last_todo = todo_list.pop()
#     redo_list.append(last_todo)

# def todo_redo(todo_list,redo_list):
#     if not redo_list:
#         print('Não a nada a refazer')
#     last_redo = redo_list.pop()
#     todo_list.append(last_redo)
#     return
    

# def do_add(todo, todo_list):
#     todo_list.append(todo)
    


# if __name__ == '__main__':

#     todo_list = []
#     redo_list = []


#     while True:
#         todo = input('Digite uma Tarefa ou [ls] para listar, [s] para sair, [undo] desfazer, [redo] refazer: ')
#         if todo == 'ls':
#             show_op(todo_list)
#             continue
#         elif todo == 'undo':
#             todo_undo(todo_list, redo_list)
#             continue
#         elif todo == 'redo':
#             todo_redo(todo_list, redo_list)
#             continue
#         elif todo == 's':
#             break
#         do_add(todo, todo_list)

    

