""" Desempacotamento de listas em Python """
# Aqui estou criando uma lista e atribuindo valores para cada elemento que nela contém. 
list = ['Santos', 'Amira', 'Lineu']

n1, n2, n3 = list

print(n2)


""" Agora se eu fizer assim, vai me gerar um erro """
# Pois tem mais elemnetos na minha lista do que os valores que atribui
# No entanto, isto pode ser resolvido através de um * , Com esse * eu crio uma outra lista dando um nome para ele, pegando o restante dos elementos
# Detalhe: Ele sempre vai encaixar no novo array tudo que vier após o * 
list = ['Santos', 'Amira', 'Lineu']

n1, n2, *newList = list

print(newList)

""" Se eu desejar Pegar somente o último item da new list """
list = ['Santos', 'Amira', 'Lineu',1,2,3,4,5,99]

n1, n2, n3, *newList, ultimoValue = list   #Atribuimos o último valor a uma new variable

print(ultimoValue)

# Detalhe tudo que vir após o encerramento do *,  sera o último valor da lista, podendo conter mais de 1
# ex:
list = ['Santos', 'Amira', 'Lineu',1,2,3,4,5,99]

n1, n2, n3, *newList, ultimoValue, ultimoValue2, ultimoValue3 = list  

print(ultimoValue, ultimoValue2, ultimoValue3)   # Pegara os ultimos 3 valores

""" Se eu não desejar pegar o restante dos valores de uma lista, mas sim algo especifico """
list = ['Santos', 'Amira', 'Lineu',1,2,3,4,5,99]

n1, n2, n3, *_ = list    #Aqui *_ estou homitindo o restante dos valores da lista

print(n1, n2, n3)  