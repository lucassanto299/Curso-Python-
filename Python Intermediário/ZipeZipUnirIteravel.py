""" Unir Iteráveis"""
""" 
----São Duas Funções----
Zip - Unindo Iteráveis (Ele sempre vai unir até a menor Lista de Todas, exclundo o restante. Ou seja, vai unir até terminar a lista menor, o restante da maior será excluido) utilizamos zip, quando não sabemos quantos valores ao certo tem na lista
Zip_longest - Itertools(Módulo). Serve para acabar com o problema de pegar apenas até o final da LISTA MENOR

- Obs: Zip_longest, você sempre precisa importar do Módulo itertools -> from itertools import zip_longest 
- ou 
- import itertools (Que trás o módulo inteiro) só que ao inves de eu usar zip_longest, eu utilizo itertools.zip_longest

- Obs 2: Zip é um gerador ou seja, consume pouca memória, mais utilizado para iterar com algo em cima de seus valores
"""

""" Unindo as Duas Listas Zip """
# cidades = ['Pelotas', 'Rio Grande', 'Porto Alegre']
# estados = ['RS', 'RS', 'RS']

# cidades_estados = zip(cidades, estados)   #Unificou as Duas Listas

# Utilizamos o For aqui, para transformar em algo a lista, que irá ser uma Tupla, se não mudar sua tipagem, não temos como ver na saída, irá aparecer apenas como Objeto. 
# for value in cidades_estados:
#     print(value)   #Vai me trazer na Tipagem de Tupla


""" Posso Converter para uma Lista """
# cidades = ['Pelotas', 'Rio Grande', 'Porto Alegre']
# estados = ['RS', 'RS', 'RS']

# cidades_estados = zip(cidades, estados)  # Podemos inverter também as "Chaves " e os "Valores" => (estados, cidades) 

# print(list(cidades_estados))  


""" Converter para um Dicionário """
# Obs:É melhor Utilizar o Zip com Listas e Não com Dicionários, pois posso ter um Terceiro Valor e Não apenas 2 para fazer Chave e Valor
# cidades = ['Pelotas', 'Rio Grande', 'Porto Alegre']
# estados = ['RS', 'RS', 'RS']

# cidades_estados = zip(cidades, estados)

# print(dict(cidades_estados))


""" Zip_longest (Módulo: itertools) """
# from itertools import zip_longest      # from: buscando o Módulo: Itertools | Import: utilizando a função zip_longest

# cidades = ['Pelotas', 'Rio Grande', 'Porto Alegre', 'São Lorenço', 'Canguçu']
# estados = ['RS', 'RS', 'RS']

# cidades_estados = zip_longest(cidades, estados)   #Agora ele irá incluir a maior Lista, porém ele vai preencher os valores que eu não mandei com None

# print(list(cidades_estados))


""" Fillvalue='' coloca um valor Padrão, para os elementos que não é passado um Valor"""
# from itertools import zip_longest        

# cidades = ['Pelotas', 'Rio Grande', 'Porto Alegre', 'São Lorenço', 'Canguçu']
# estados = ['RS', 'RS', 'RS']

# cidades_estados = zip_longest(cidades, estados, fillvalue='Estado')   #Coloquei um Argumento nomeado, para dar um valor padrão

# print(list(cidades_estados))


""" Criando Mais Um Indice para add junto com as nossas Cidades neste exemplo """
""" Vamos utilizar o Módulo Count. Count: Count sem um Parâmetro(): É simplesmente um contador ou seja, conta para mim 0,1,2,3,4,5,6 etc.. Mas ele também é um gerador e consome poucos recursos da Memória"""
from itertools import zip_longest, count     

indice = count()   #Count sem um parâmetro é simplesmente um contador   | Essa minha variável indice, é um gerador ou seja, me entrega um valor de cada vez
cidades = ['Pelotas', 'Rio Grande', 'Porto Alegre', 'São Lorenço', 'Canguçu']
estados = ['RS', 'RS', 'RS']

cidades_estados = zip(      #Utilizamos a função zip, porque iria dar conflito com nosso gerador count, iria ficar gerando valor infinitamente, ele iria ficar contando no modo infinit ou seja, iria dar conflito
    indice,
    cidades, 
    estados, 

)   

# Fazendo um for, para ficar melhor a visualização (linha, por linha)

# for valor in cidades_estados:  #Vai me retornar uma Tupla com 3 valores, sendo um deles meu contador, que é serve só para demonstrar o indice neste caso
#     print(valor)   #

""" Se eu quiser desempacotar isso com 3 variáveis(uma tupla com 3 valores) """
for indice, cidades, estados in cidades_estados:
    print(indice, cidades, estados)