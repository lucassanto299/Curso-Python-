""" List Comprehension """

""" Serve para fazer: Com base em um Iteravel 
gerar Outro Iteravel e fazer algum processamento de dado no Caminho 
"""

""" Com List Comprehension """
# numeros = [1,2,3,4,5]

# copia_numeros = [numero for numero in numeros]

# print(copia_numeros)


""" Sem List Comprehension """
# numeros = [1,2,3,4,5]

# copia_numeros = []   #Para poder pegar os valores que foram jogados aqui
# for numero in numeros: 
#     copia_numeros.append(numero)  # Estou jogando os valores dentro do copia_numeros

# print(copia_numeros) # E aqui consigo puxar fora do meu for todos valores. 


""" Outro Exemplo Divisão """
# Divindo os valores da Minha lista, sem afetar está lista Original.
# Basicamente é como se fosse o map, estou mapeando uma lista para outra lista 
# Só que no meio do caminho estou fazendo o processamento antes de gerar os dados em uma nova lista
# numbers = [1,2,3,4,5]

# division = [div / 2 for div in numbers]
# multiplication = [multiplication * 2 for multiplication in numbers]
# potentiation = [potentiation ** 2 for potentiation in numbers]

# print(division)
# print(multiplication)
# print(potentiation)


""" Podemos jogar isso para uma Função também, tornando reutilizavel em qualquer parte do código com isto """
# def divisionList(x,y):
#     return x / y

# def multiplicationList(x,y):
#     return x * y

# def potentiationList(x, y):
#     return x ** y

# numbers = [1,2,3,4,5]

# division = [divisionList(div, 2) for div in numbers]
# multiplication = [multiplicationList(multiplication, 2) for multiplication in numbers]
# potentiation = [potentiationList(potentiation, 2) for potentiation in numbers]

# print(division)
# print(multiplication)
# print(potentiation)


"""  
Quando fizemos "Map"

Podemos pegar tudo que esta em uma lista e joga em outra lista
E podemos processar esses dados como vimos anteriormente.

Obs: Tudo que esta em uma Lista, vai passar para uma outra Lista
Você processando ou não os dados, este valor estara em uma nova lista.
"""

""" ---------------------------------------------------------------------------------------- """

""" Aplicando o "Filter" """
""" 
Na List Comprehension eu tenho dois Lugares Diferentes para colocar o IF para fazer o Filtro

- Antes do For Se for uma Operador Ternário
- Após o For se eu desejar Filtrar (Forma Mais Comum) 

"""

# numbers = [1,2,3,4,5,6,7,8,9,10]

# minors = [number for number in numbers if number < 5]
# odd = [odd for odd in numbers if odd % 2 != 0]    #Se o número não for diferente de 0
# pairs = [pair for pair in numbers if pair % 2 == 0]
# different_6 = [number if number != 6 else 600 for number in pairs]   #Reutilizei meu Paires aqui, já filtrando os números Pares, sem precisar fazer mais um if 

# # Neste caso agora eu vou utilizar 2 IF Ou Operador Ternario, se não for isso, faça isso.
# # Quero trocar todos números 6 do meu filtro para 6 | Toda vez que o número não for diferente de 6, vai se tornar 600
# # Se o número for Diferente de 6, como ele não vai ser na condição tradicional, coloco direto para pegar o valor que eu desejo

# print(minors)
# print(odd)
# print(pairs)
# print(different_6)


""" Linhas E Colunas (Mais conhecido como: For Alinhado / Um For Dentro do Outro) """
""" Cada elemento da minha coluna que é X, ele vai repetir 5 vezes meu laço for, que serão 5 linhas y """
""" Desta forma, iremos gerar um For alinhado de X e Y """
# for x in range(10):
#     for y in range(5):
#         print(x,y)


""" Podemos fazer isso com List Comprehension também  """
# Obs: Sempre que você coloca um for e depois outro na List Comprehension, eles são alinhados ou seja
# Um for dentro do outro.
""" No entanto, neste caso eu já irei gerar uma Tupla, com o x e y """
# Neste caso eu vou ter 2 valores X e Y, portanto, vou ter que gerar Dois For em List Comprehension
# Se não fosse List Comprehension, não precisaria.

# linhas_e_colunas = [
#     (x, y)
#     if y != 2 else (x, y * 1000)   #Neste caso, estaria só multiplicando o Y
#     for x in range(1, 11)
#     for y in range(1, 6)
#     if x != 2   #Neste caso, se o x não tiver o valor diferente 2, ele não vai mais aparecer, pois irá me retornar o Valor Falso
# ]

# print(linhas_e_colunas)


""" List Comprehension Com Strings """
# string = 'Lucas Santos'
# jump_letter = 2

# new_string = '.'.join([string[index: index + jump_letter] for index in range(0,len(string), 2)])   #O Join, é a cada pulo de 2, ele vai colocar um . e vai juntar os valores.

# print(new_string)


""" Ex 2 """
# names = ['Lucas', 'Amira', 'Lineu', 'Matheus', 'QualquerNome']
# names_upper = [name.upper() for name in names]
# names_lower = [name.lower() for name in names]
# first_upper = [name.title() for name in names]
# last_upper = [f'{name[:-1].lower()}{name[-1].upper()}' for name in names]
# print(last_upper)


""" Ex 3 """
numbers = [[number, number ** 2] for number in range(10)]
flat = [y for x in numbers for y in x]   #Só para não ter uma lista dentro de outra lista

print(numbers)
print(flat)