""" Expressões lambda (Funções anônimas) em Python """
"""--- Função Normal ---"""
def func(value, value2):

    return value * value2

result = func(2,2)
print(result)

""" Função Lambda/Anônima/Arrow function """
result = lambda value, value2: value * value2
print(result(2,2))

""" Funções Lambda é mais Usado Para passar uma função por Parâmetro para Outra Função or Método de alguma Classe """
""" Ordenando esta Lista por Preços, existem dois Modos em Python"""
""" 1- list.sort() """
list = [
    ['Produto 1', 13],
    ['Produto 2', 6],
    ['Produto 3', 7],
    ['Produto 4', 50],
    ['Produto 5', 8]
]

list.sort()   #Estou alterando a ordem da Lista que acabei de criar
print(list)   #Porém não irá acontecer a alteração neste caso, pois tenho outras listas Dentro da minha lista

""" Mas se eu fizer assim, vai funcionar a Alteração """
""" E esta pegando do preço mais baixo ao mais alto desta maneira. """
list = [
    ['Produto 1', 13],
    ['Produto 2', 6],
    ['Produto 3', 7],
    ['Produto 4', 50],
    ['Produto 5', 8]
]
def func(item):
    return item[1]   #Aqui estou ordenando pelo Preço, pois esta pegando do indice 1 da lista, o 0 é o produto. 
                    
list.sort(key = func)   #Estou alterando a ordem da Lista que acabei de criar, através da minha função
print(list)  

""" Se eu desejar pegar do preço mais alto, basta fazer um: reverse = True """
list.sort(key = func, reverse = True)   #Agora com reverse = True, reverteu do preço mais baixo, para o Mais alto.
print(list)  

""" Fazendo isso com Lambda, não precisariamos criar uma função só para ordenar a lista """
list = [
    ['Produto 1', 13],
    ['Produto 2', 6],
    ['Produto 3', 7],
    ['Produto 4', 50],
    ['Produto 5', 8]
]

list.sort(key= lambda item: item[1], reverse=True)   #Se eu não quiser do Maior para o Menor, basta tirar o Reverse
""" or """
print(sorted(list, key= lambda item: item[1]))