""" Tuplas em Python """
""" Utilizamos Tuplas, quando queremos só para leitura de um objeto, sem modifcações nele """
""" A diferença de Tuplas para Listas, é que você não pode Editar os Elementos das Tuplas """
""" 
- Não pode Adicionar Elementos
- Não pode Remover Elementos 
- Não pode Mudar o Valor Do Indice da Tupla
"""
""" Criar uma Tupla """
value = (1,2,3, 'a', 'Lucas Santos')    #Aqui esta minha Tupa, posso adicionar elementos na criação dela
print(type(value))   #Esta me mostrando o tipo de Value, que é do tipo Tupla
print(value)    #Me Mostrando os Valores que tem na Tupla

""" Se eu desejar acessar algum Elemento da minha Tupla """
""" Basta chamar pelo Indice """
value = (1,2,3, 'a', 'Lucas Santos')   
print(value[1])    #Chamando pelo indice

""" Se eu desejar Iterar sobre este elementos da Tupla """
""" Cada iteração deste meu Laço, eu irei ver um elemento da Minha dupla """
value = (1,2,3, 'a', 'Lucas Santos')
for i, element in enumerate(value):    #Coloquei um enumerate só para vermos a enumeração dos indices
    print(i,element)

""" Se eu desejar fatiar minha Tupla """
value = (1,2,3, 'a', 'Lucas Santos')
print(value[1:])  #Estou dizendo para me mostrar do Indice 1 em diante.

""" Posso ter Tupla Sem Parênteses também """
value = 1,2,3, 'a', 'Lucas Santos'
print(value)

""" No entando Eu preciso Utilizar uma Virgula, mesmo que Só tenha um Elemento """
""" Não se torna uma Dupla sem uma , """
value = 1,   #Mesmo deste jeito, será uma Tupla, por conta da virgula.
print(type(value))

""" Concatenar Tupla """
value = 1,2,3,4
value2 = 5,6,7,8
# value += value2
# print(value)
""" ---Or--- """
value3 = value + value2
print(value3)

""" Desempacotar """
value = 1,2,3,4
value2 = 5,6,7,8
value3 = value + value2

n1,n2,n3, *_ = value3
print(n3)
"""---Se eu quiser pegar o ultimo elemento---"""
value = 1,2,3,4
value2 = 5,6,7,8
value3 = value + value2

n1,n2,n3, *_, n8 = value3    #Aqui estou pegando o ultimo elemento.
print(n8)

""" Repetir o Valor da Tupla com Modificador """
value = (1,2,3,4,5) * 20    #Aqui *20 estou colocando meu modificador e dizendo para ele Repetir 20 vezes os valores que estão nas Tuplas
print(value)

""" Converter Tuplas em Listas """
value = (1,2,3,4,5)
value = list(value)
print(value)

"""---Para ela voltar ser uma Tupla---"""
value = (1,2,3,4,5)
value = list(value)    #Passei para uma lista, para modifcar seu valor
value[1] = 10   #Modifquei o seu valor, pois passei para uma lista
value = tuple(value)   #Retornei agora para uma Tupla novamente. Com o valor modificado
print(value)



