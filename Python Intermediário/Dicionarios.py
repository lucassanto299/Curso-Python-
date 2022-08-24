""" Dicionários em Python """
""" Os dicionários são muito similares a listas """
"""
- Ele tem um Índice 
- Ele tem um Valor
"""
""" 
A diferença de um Dicionário para Listas em Python 
Nas listas, o Python gera um Índice para Você 0,1,2,3 etc..
- Mas no Dicionario, você controla os Índices, também chamado de Chave
Ou seja:
- Um dicionário é uma estrutura de Dados que suporta um Par de Chave e Valor
- Sempre que eu criar um Dicionario eu preciso falar:
-- Chave
-- Valor
Sendo "Chave" o Índice do Dicionário
Chaves dentro do Dicionário precisam ser únicas ou seja, uma única chave com o mesmo nome
"""

""" Criando um Dicionário """
dicionario = {'chave1': 'Lucas Santos'}
print(dicionario)

""" Adicionado Uma Nova Chave """
dicionario = {'chave1': 'Lucas Santos'}
dicionario['Nova_chave'] = 'Valor Da Nova Chave'    #Agora ele vai ter a chave 1 e uma Nova chave que é a 2
print(dicionario)

""" Chamando por Chave Específica """
dicionario = {'chave1': 'Lucas Santos'}
dicionario['Nova_chave'] = 'Valor Da Nova Chave'   
print(dicionario['chave1'])    #Aqui eu abri meu objeto dicionário e estou chamando por uma chave específica 

""" Outro Modo de Criar um Dicionário """
""" Através do construtor dict """
dicionario = dict(chave1 = 'Valor da Chave', chave2 = 'Valor Da Segunda chave')    #Aqui estou colocando o construtor dict, tornando não mais necessário colocar {}
dicionario['chave1'] = 'Novo Valor da chave 1'    #Estou criando um novo valor para a Chave1
print(dicionario)

""" Para Chaves podemos Utilizar qualquer Tipo de dado Imutável """
""" Geralmente Iremos ver Strings/str """
""" 
- Podemos usar Str
- Numbers
- Tuplas
"""
d1 = {
    'str' : 'Valor da String',
    123 : 'Valor do Number',
    (1,2,3,4) : 'Valor da Tupla',
}

print(d1[(1,2,3,4)])    #Abri o objeto dicionário [], chamei a minha chave que é uma tupla ()

""" Se eu tentar chamar uma Chave Que não existe, meu código para na hora """
""" Ou seja, ele não continua o processsamento dos restante dos códigos abaixo """
""" Para contornar isto, basta criar a chave que não existe, ou fazer um uma condição """
""" Utilizando IF in ou not in """
d1 = {
    'str' : 'Valor da String',
    123 : 'Valor do Number',
    (1,2,3,4) : 'Valor da Tupla',
}
print(d1['naoexiste'])    #O código pararia aqui e não executaria o restante
print('Oi!')     #Não vai ser executado

""" Criando a chave que não existe """
d1 = {
    'str' : 'Valor da String',
    123 : 'Valor do Number',
    (1,2,3,4) : 'Valor da Tupla',
}
d1['naoexiste'] = 'Agora existe'
print(d1['naoexiste'])    #Agora será executado 
print('Oi!')     #E este código que está a baixo será mostrado

""" Daria para solucionar com If in ou in not """
d1 = {
    'str' : 'Valor da String',
    123 : 'Valor do Number',
    (1,2,3,4) : 'Valor da Tupla',
}
if 'naoexiste' in d1:
    print(d1['naoexiste'])    #Agora não irá gerar erro por conta da condição que vai me retornar Falso, rementendo ao código a baixo sendo executado   
print('Oi!')          #Sera executado

""" Outra Maneira é utilizando .get """
d1 = {
    'str' : 'Valor da String',
    123 : 'Valor do Number',
    (1,2,3,4) : 'Valor da Tupla',
}
print(d1.get('nomedachave'))    #Não irá me retornar um erro e parar meu processamento, pois estou utilizando método get, para retornar um valor especifoc com a chave que neste caso será: None.
print('Oi!')    #Sera executado

""" Utilizando if is not agora """
d1 = {
    'str' : 'Valor da String',
    123 : 'Valor do Number',
    (1,2,3,4) : 'Valor da Tupla',
}
if d1.get('nomedachave') is not None:    # Se o valor não for None, mostre.
    print(d1.get['nomedachave'])    #Não irá mostrar, porque não tem valor

print('Oi!')   #E irá ser mostrado meu print

"""---Mas se eu criar ela agora---"""
d1 = {
    'str' : 'Valor da String',
    123 : 'Valor do Number',
    (1,2,3,4) : 'Valor da Tupla',
}
d1['nomedachave'] = 'Agora tem valor'
if d1.get('nomedachave') is not None:   
    print(d1['nomedachave'])    

print('Oi!')  

""" Maneira de Adicionar ou Atualizar o Valor de uma Chave """
""" Se eu desejar mudar o valor de uma Chave que já existe """
d1 = {
    'str' : 'Valor da String',
    123 : 'Valor do Number',
    (1,2,3,4) : 'Valor da Tupla',
}

d1['str'] = 'Agora tem valor'    #Aqui eu mudei/atualizei o valor de uma chave que já existe, se ela não existisse, eu simplemente iria criar uma chave com um valor.

if d1.get('str') is not None:   
    print(d1['str'])    

print('Oi!')  

""" Outra Maneira é através da função .update() """
d1 = {
    'str' : 'Valor da String',
    123 : 'Valor do Number',
    (1,2,3,4) : 'Valor da Tupla',
}
d1.update({'Nova chave': 'Novo Valor da Nova Chave'})   #Acabei de criar uma nova chave por conta da função .update()

if d1.get('Nova chave') is not None:   
    print(d1['Nova chave'])    

print(d1)

""" Excluindo Uma Chave """
d1 = {
    'str' : 'Valor da String',
    123 : 'Valor do Number',
    (1,2,3,4) : 'Valor da Tupla',
}

del d1['str']    #del chamo dicionário e abro ele, e digo qual chave desejo excluir
print('str' in d1)    #Estou verificando se esta chave ainda existe, vai me retornar um valor bloeano

"""---Verificar a existencia de um Valor--- """
print('Valor do Number' in d1.values())    #Através do values() eu checo os valores das minhas chaves, digo qual eu quero verificar especificamente.

"""---Verificando a Existencia de Uma Chave---"""
print(123 in d1.keys())    #Estou verificando a existencia da chave
""" Or """ 
print(123 in d1)           #Da mesma forma aqui

""" 
Como isso tudo irá me retornar um Valor Boleano, eu posso passar para IF, Else, 
"""
""" Se eu desejar Saber quantos Par de chaves eu tenho, com seus respectivos valores """
# print(len(d1))

""" Iterar sobre o Dicionário """
d1 = {
    'chave' : 'Valor da String',
    'chave 2' : 'Valor do Number',
    'Chave 3' : 'Valor da Tupla',
}
"""---Iterar apenas sobre as Chaves---"""
for k in d1:
    print(k)

"""---Iterar apenas Sobre os Valores---"""
for k in d1.values():    #Uso a função values
    print(k)

"""---Iterar sobre Chaves e Seus Valores  """
for k in d1.items():    #Irá me retornar Tuplas
    print(type(k))   #Eu fazendo minha saída desta maneira
    print(k[0], k[1])    #Já desta maneira especifica, me retornaria a tipagem original   

""" Forma mais Usual de desempacotar isso é Assim """
for k, v in d1.items():    #Estou sinalizando que quero 1 primeiro e segundo valor de cada indice do Dicionário: Chave e Valor
    print(k, v)    #Estou mostrando Chave e Valor de cada índice do dicionario. 

""" Fazendo um Dicionário de Clientes com ID, com dicionário de Cada Cliente """
""" Modo Crio Dicionários Dentro de Dicionários """
clients = {
    'Cliente 1' : {
        'Name' : 'Lucas',
        'Last Name' : 'Santos',
    },
        'Cliente 2' : {
            'Name' : 'Amira',
            'Last Name' : 'Ahamad',
    },
}
"""---De Maneira Grosseira---"""
for k, v in clients.items():
    print(k, v)

"""---Da Maneira mais Usual---"""
""" Modo que eu Faço a Iteração de Dicionários que tem como Filho Outors Dicionários """
for clients_k, clients_v in clients.items():
    print(f'Exibindo {clients_k}')
    for dados_k, dados_v in clients_v.items():
        print(f'\t{dados_k} = {dados_v}')    #Este \t é só para dar o Tab na linha

""" Fazendo Copias Para Modificar Somente a Copia e Não O Dicionário Original """
""" Pois Dicionários em Python, os dois Apontam para o mesmo local Na memória """
"""---Ambos Ficaram com mesmo Valor Modificado Desta Maneira---"""
d1 = {1: 'a', 2 : 'b', 3 : 'c'}
v = d1
v[1] = 'Lucas Santos'    #Aponta para o mesmo Local na memória do d1, por isso também será Modificado lá
print(d1)
print(v)
print(v == d1)   #Irá me mostrar um valor Booleano que ambos apontam para o mesmo local

""" Fazendo uma Cópia do Dicionário Raza .copy()"""
d1 = {1: 'a', 2: 'b', 3: 'c', 'd' : ['Lucas', 'Santos']}
v = d1.copy()    #Acabei de fazer uma Cópia raza do meu D1, colocando esta cópia dentro da Variável V

v[1] = 'Santos'    #Estou modificando o valor da chave 1 da na cópia

print(v['d'][0])   # Estou chamando o primeiro item da minha lista que esta na chave d

print(d1)
print(v)

"""---No entanto, se eu tentar modificar minha Lista que esta dentro da chave D---"""
"""--Também irá alterar meu dicionário Original, Pois é uma Cópia Raza--"""
d1 = {1: 'a', 2: 'b', 3: 'c', 'd' : ['Lucas', 'Santos']}
v = d1.copy() 
v[1] = 'Santos'    #Estou modificando o valor da chave 1 da na cópia

v['d'][0] = 'MudouNome'   # Estou chamando o primeiro item da minha lista que esta na chave d

print(d1)
print(v)

""" Fazendo uma Cópia Real/Cópia Profunda de Um Dicionário import_copy"""
""" Módulo import_copy eu utilizo a função copy.deepcopy, ao invés da função copy() apenas """
"""-- O sinal de Atribuição não faz uma cópia necessáriamente, mas sim fazendo uma referência"""
# A diferença entre cópia profunda e rasa é relevante apenas para objetos compostos (objetos que contêm outros objetos, como listas ou instâncias de classe)
import copy
d1 = {1: 'a', 2: 'b', 3: 'c', 'd' : ['Lucas', 'Santos']}
v = copy.deepcopy(d1)    #Aqui estou fazendo uma Cópia Profunda, podendo alterar objetos que estão dentro de outros objetos.

v[1] = 'Santos'    
v['d'][0] = 'MudouNome'   

print(d1)
print(v)

""" Com Tupla """
"""--Desta Maneira irá me gerar um Erro, pois Tupla, não pode ser alterado--"""
import copy
d1 = {1: 'a', 2: 'b', 3: 'c', 'd' : ('Lucas', 'Santos')}    #Aqui irá me gerar um erro, pois não posso modificar uma Tupla desta Maneira.
v = copy.deepcopy(d1)   
v[1] = 'Santos'    
v['d'][0] = 'MudouNome'   

print(d1)
print(v)

"""--Mas posso alterar o Valor de uma Tupla com Outra--"""
import copy
d1 = {1: 'a', 2: 'b', 3: 'c', 'd' : ('Lucas', 'Santos')}   
v = copy.deepcopy(d1)   
v[1] = 'Santos'    
v['d'] = ('MudouNome', 'Outro valor')    #Desta maneira eu posso alterar minha Tupla, pois só pode ser alterada com outra da mesma. 

print(d1)
print(v)

""" Fazendo Casting/Fundição/Converter """
"""--Casting com o Construtor dict()--"""
# Posso converter esta lista, porque tenho um Par de valores aqui, pois fica similar a chaves e valores
list = [
    ['Item 1', 1],
    ['Item 2', 2],
    ['Item 3', 3],
]

d1 = dict(list)    #Acabei de converter minha lista em um Dicionário
print(d1)

"""--Posso Converter também Tuplas dentro de Listas or Listas dentro de Tuplas--"""
# Posso converter esta lista, porque tenho um Par de valores aqui, pois fica similar a chaves e valores
list = [
    ('Item 1', 1),
    ('Item 2', 2),
    ('Item 3', 3),
]
list2 = (
    ['Item 1', 1],
    ['Item 2', 2],
    ['Item 3', 3],
)

d1 = dict(list)    #Converti Tuplas dentro de Listas para um Dicionário
d2 = dict(list2)   #E aqui uma lista dentro de Tuplas
print(d1)
print(d2['Item 3'])   #Acessando algo especifico, só para lembrar :P

""" Função .pop() e popitem() em Dicionários """
"""--Só é um pouco diferente das listas--"""
"""- .pop() eu preciso referenciar qual chave eu quero que Elimine -"""
d1 = {
    1: 'Value 1',
    2: 'Value 2',
    3: 'Value 3',
}

d1.pop(3)   #Estou eliminando a chave que estou indicando na minha função .pop()
print(d1)

"""- .popitem() Elimina o último item qualquer que seja ele -"""
d1 = {
    1: 'Value 1',
    2: 'Value 2',
    3: 'Value 3',
}

d1.popitem()   #Elimina qualquer ultimo item 
print(d1)

""" Concatenando Dicionários .update()"""
"""--Através da Função .update()--"""
d1 = {
    1: 'Value 1',
    2: 'Value 2',
    3: 'Value 3',
}

d2 = {
    'a': 'primeiro',
    'b': 'segundo',
    'c': 'terceiro',
}
d1.update(d2)   #Aqui estou concatenando meu dicionário d2, dentro de d1
print(d1)

