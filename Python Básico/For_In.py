# For in em Python 
""" 
Iterando strings com for 
função range (start=0, stop, step=1)
"""
# Exemplo: Diferença do while para o for na iteração de uma string.
# while: Aqui ele esta exibindo cada caracter em uma linha.

texto = 'Python'

acc = 0
while acc < len(texto):  # Aqui eu sei o número de índices por completo da minha string
    print(texto[acc], acc)
    acc += 1 #Toda vez que ele passar por aqui, vai para o próximo índice, pois estou incrementando +1


# # Agora com laço for: Estou dizendo aqui: For: para / letra: cada letra / in texto: em texto/ : faça/
texto = 'Python'  # print: mostre letra | Ou seja, vai pegar por completo minha string
for letra in texto:   
    print(letra)

# Com acc enumerate:
texto = 'Python'
for n, letra in enumerate(texto):
    print(n,letra)

# # Utilizando a função range, podemos utilizar ela junto com laço for, porém as duas são independentes.
for numero in range(10):  #Aqui a função range vai contar de 0-9
    print(numero)

# Se desejarmos altear o padrão da função: 
for n in range(20,10,-1):
    print(n)


# Bom para saber multiplos também: Multiplos de 8 Ex:
for n in range(0,100,8):
    print(n)

# Também podemos fazer desta forma com range e if: 
for n in range(100):
    if n % 8 == 0:
        print(n)


# Se eu desejar iterar sobre uma string: 
texto = 'Python'
novaString = ''

for letra in texto:
    if letra == 't':
        novaString += texto.upper() 
    elif letra == 'h':
        novaString += letra.upper
    else:
        novaString += letra
print(novaString)

# Aqui também podemos utilizar as palavras continue e break 

texto = 'Python'
novaString = ''

for letra in texto:
    if letra == 't':
        continue
        novaString += letra.upper() 
    elif letra == 'h':
        novaString += letra.upper()
        break
    else:
        novaString += letra
print(novaString)