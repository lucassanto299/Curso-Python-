""" Geradores, Iteradores e Iteráveis em Python """

""" Iteravel """
# Se for iteravel, podemos utilizar o For, para exibir os valores da lista. Tornando assim, um objeto iteravel.
""" 
- Lista
- String
"""

""" Lista (Um Objeto Iteravel) """
#Se eu quiser saber se algo é iteravel eu posso utilizar
# A função hasattr() passo a minha lista para dentro da função
# E verifico se tem o método '__iter__', Este método irá me retornar um valor boolean, verifcando se é iteravel ou não
# lista = [0,1,2,3,4,5]
# print(hasattr(lista, '__iter__'))


""" Porém se eu mudar para Números (Não é iteravel) """
# Irá me retornar a falso
# lista = 12345
# print(hasattr(lista, '__iter__'))


""" Iterador """
""" 
- For
"""
# Neste caso, o laço for transforma nossa Lista em um Iterador, ai ele utiliza esse iterador para que ele possa exibir cada valor em uma linha/Separadamente.
# lista = [0,1,2,3,4,5]

# for v in lista:   #Passamos uma variavel que é V/ falamos a lista que Nós queremos in Lista, e falamos a Variável que é para o For jogar o Valor que é V
#     print(v)   #E ai ele joga esse valor um de cada vez na nossa variável V, cada passada do laço pega um valor. Ou seja, ele transforma a Lista em um Iterador e a Lista não é um Iterador

# # Se eu desejar saber se um Elemento é Iterador eu faço (hasattr(lista, '__next__'))
# print(hasattr(lista, '__next__'))  #Retorna um valor boolean

# O que o For faz para Lista ser um iterador é usar a função Iter/Método __iter__ 
# Mas podemos simular isso fazendo assim: iter(lista)
# lista = iter(lista)
# print(hasattr(lista, '__next__'))

""" Next """
# lista = [0,1,2,3,4,5]
# lista = iter(lista)

# print(next(lista))
# print(next(lista))   #Next, vai me trazer sempre o próximo elemento da minha lista.
# print(next(lista))
# print(next(lista))


""" Geradores """
""" (São usados geralmente quando precisamos de usar valores que irão utlizar muita memória ou muito tempo para ser feito) 
"""
import sys
# lista = list(range(1000))  #Uma lista neste caso aqui, recebe todos os valores de uma vez, neste caso Mil valores e salvado na memória, Números muito grandes de bits em uma lista não é o ideal
# Se você esta lidando com um servidor com menos recursos ou você quer Otimizar seu código, não é ideal você ter uma lista com Mil valores na memória, por isso, surge os gerados em Python
# Ou seja, não precisamos de todos os valores ao mesmo tempo.
# print(sys.getsizeof(lista))   #Estou pegando, quantos bits esta lista esta consumindo de memória do meu Computador ou de um servidor

""" Ex 1 """
# def gera():
#     r = []
#     for v in range(100):
#         r.append(v)
#     return r

# g = gera()

# for v in g:
#     print(v)

""" Passando Esta função para uma Função Geradora Para ela Gerar um Iteravél e Ai ela vai me Retornar um Elemento Por vez, não precisando esperar por todos os valores a serem preenchidos na lista """
# A diferença deste para o anterior, é que este vai retornar um valor de cada vez, sem esperar todos os valores serem preenchidos da minha lista, conforme vai recebendo, já vai jogando.
# def gera():
    
#     for v in range(100):
#         yield v   #Neste momento, minha função, se torna um Gerador
        
# g = gera()
# for v in g:
#     print(v)

""" Os iteradores, ao contrário dos iteraveis, os iteradores tem o método Next """
""" Eles tem o modo Next e iter que é iteradores """
# print(hasattr(g, '__iter__'))   # Vai ser Verdadeiro
# print(hasattr(g, '__netx__'))   #Vai ser Verdadeiro

""" Portanto, posso utilizar o Método Next """
""" Pegar cada valor, apenas utilizando a função Next (Não precisando Pegar a Lista inteira) """
""" Cada vez que eu Utilizar next, irei ver um Novo Valor """
# print(next(g))
# print(next(g))
# print(next(g))


""" Outra coisa que eu Posso Fazer Sem Precisar Utilizar o For """
""" Fazendo uma função que a cada vez que chame ela, ela me retorne o próximo valor """
""" Melhor maneira de Utilizar isso é com Laço For """
# def gera():
#     variavel = 'Valor 1'
#     yield variavel 
#     variavel = 'Valor 2'
#     yield variavel 
#     variavel = 'Valor 3'
#     yield variavel 

# g = gera()

# print(next(g))
# print(next(g))
# print(next(g))

""" Ex 2 """
l1 = [x for x in range(10000)]
l2 = (x for x in range(1000))   #Esta é a melhor forma de criar um gerador é trocar na list comprehension [] para  () sem ter que utilizar função

print(sys.getsizeof(l1))   #A primeira lista esta usando 8856 byts na minha mémoria | As listas irão reter todos os valores que você mandar nela e salvar na memória
print(sys.getsizeof(l2))   #A segunda lista continua usar 104  | Os geradores irão reter todos os valores, mas não irão salvar na memória. 
# Ele só vai lhe entregar um valor quando você pedir usando a função Next ou For
