""" Count - Contadores infinitos em Python """
""" 
Count = Itertools
Função Count: Vai te gerar um contador, que é um iterador. Portanto, você pode usar a função next() com este contador. Diferente da função range, que não é um iterador, a função range é um iteravel, mas não é um iterador
"""
""" 
Exmplo: 
Digamos que você queira gerar um contador que conte até 10, ou que pule, ou 0 -10  etc.. 
Qualquer tipo de contador, você pode utilizar esta função aqui.
"""
from itertools import count

# contador = count()  #Este contador, ele é um iterador. Portanto posso dar um print(next(contador)) pois essa função count() não tem fim, ela conta até o infinito
# print(next(contador))    #Como eu não passei nenhum parâmetro para meu contador: count(parametro), ele vai começar em 0 e vai incrimentando de um em um, até o infinito. Obs: Cuidado para não ter um loop-infinito
# print(next(contador))
# print(next(contador))
# print(next(contador))


""" Cuidado para não ter um loop-infinito """
# Ex:
# contador = count() 

# for valor in contador:   #Como ele é um contador-Iterador que não tem fim. 
#     print(valor)         #A cada vez que eu pedir um valor para ele, ele vai me entregar um valor. Pois o for sempre irá pedir o próximo valor para o contador, e com tador sempre irá entregar um próximo valor para o for, iremos ter o famoso laço-infinito


""" Se eu desejar para esse Laço-infinito, basta fazer uma condição IF """
# Ex:
# contador = count() 

# for valor in contador:   #Como ele é um contador-Iterador que não tem fim. 
#     if valor < 11:
#         break

""" O contador também tem um Start=value Da onde eu quero iniciar """
# # Ex:
# contador = count(start=5)   #Estou falando de onde eu quero que meu contador inicie 

# for valor in contador:   #Como ele é um contador-Iterador que não tem fim. 
#     print(valor)    
    
#     if valor >= 10:   #Neste caso, eu estou quebrando o laço no 10, para não ser infinito
#         break


""" Se eu desejar que ele Pule step = value """
# Ex:
# contador = count(start=5, step=2)   #Estou falando de onde eu quero que meu contador inicie e quantas vezes eu quero que pule cada indice

# for valor in contador:  
#     print(valor)    
    
#     if valor >= 10: 
#         break


""" Se eu desejar que pegue Com Casas decimais (float)"""
# contador = count(start=5, step=0.1)   #Estou mandando número de ponto flutuante agora irá ficar: 5, alguma coisa

# for valor in contador:  
#     print(round(valor,2))  #Usei a função round, para arredondar com 2 casas decimais  
    
#     if valor >= 10: 
#         break


""" Posso contar de Forma Invertida também (De Trás para Frente) """
# contador = count(start=0, step=-1)   #Vai pegar de forma Invertida

# for valor in contador:  
#     print(round(valor,2))  
    
#     if valor >= 10 or valor <= -10:   #Aqui estamos contando negativamente
#         break


""" Agora supondo que eu tenho uma Lista de nomes """
""" Eu quero indexar esta lista, colocar um indice para cada elemento desta lista """

""" 
Ou seja, o Python já tem um contador pronto, a única coisa que você tera que fazer
É colocar 2 linhas de código:

- from itertools import count
- contador = count()

"""
contador = count()
lista = ['Lucas', 'Santos', 'Amira', 'Lineu', 'Mateus', 'Kaleu']

lista = list(zip(contador, lista))  #Aqui eu indexei minha lista, isso é bom, pois cada elemendo que eu adicionar na minha lista, eu já irei ter um indice para o novo elemento
print(lista[1])








# """ Para saber se algo é um Gerador """
# from types import GeneratorType

# variavel = zip('Alo', 'Alo')    #String é Iteravel e a função zip retorna um iterador que podemos chamar assim next(variavel)  #Ai pego meu elemento, exemplo, variavel. Que contenha a função zip() com dois Iteradores
# print(next(variavel))   #Isso é um iterador que lhe entraga um valor de cada vez
# print(list(variavel))

# print(isinstance(variavel, GeneratorType))   #Estou perguntando, a variável é de uma instancia de generator/gerador desse tipo/type 


# """ Transformando isso: variavel = zip('Alo', 'Alo') Em um Gerador """
# variavel = ((x,y) for x, y in zip('Alo', 'Alo'))  #Agora se tornou um gerador
# print(isinstance(variavel, GeneratorType))
# print(list(variavel))
