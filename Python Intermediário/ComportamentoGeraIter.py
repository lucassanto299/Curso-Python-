""" Comportamento de Geradores e Iteradores """
""" 
O comportamento dos Geradores para os Iteradores são diferentes:
- O for, ele converte em tempo de execução a minha string em um Iterador, pois aí o for vai utilizar o Next, até pegar todos valores da minha String
- Se eu converter para um Iterador diretamente pelo iter(), basta eu chamar na saída o Next
"""
# List, Tuplas, str => São sequencias -> Iteravel | Pode utilizar for, chamar por indice etc..
nome = 'Lucas Santos'
iterador = iter(nome)
gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

for letra in gerador:   #Esta pegando o restante do gerador
    print(letra)



""" Para saber se algo é um Gerador """
from types import GeneratorType

variavel = zip('Alo', 'Alo')    #String é Iteravel e a função zip retorna um iterador que podemos chamar assim next(variavel)  #Ai pego meu elemento, exemplo, variavel. Que contenha a função zip() com dois Iteradores
print(next(variavel))   #Isso é um iterador que lhe entraga um valor de cada vez
print(list(variavel))

print(isinstance(variavel, GeneratorType))   #Estou perguntando, a variável é de uma instancia de generator/gerador desse tipo/type 


""" Transformando isso: variavel = zip('Alo', 'Alo') Em um Gerador """
variavel = ((x,y) for x, y in zip('Alo', 'Alo'))  #Agora se tornou um gerador
print(isinstance(variavel, GeneratorType))
print(list(variavel))
