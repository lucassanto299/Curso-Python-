# Manipulando Strings 

""" 
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc..
Essas funções podem ser usadas diretamente em cada tipo.
"""

# Positivos
texto = 'Python s2'
print(texto[1])  #Ele vai pegar o y

# Negativos
print(texto[-1]) # Ele vai pegar o 2


# Fatiamento de String
novaString = texto[7:9] # Falei para ele começar com índice 7 e terminar no índice 9, restultado: s2
print(novaString)

novaString = texto[:-2] # Vai pegar todo inicio e eliminar os últimos dois índices
print(novaString)


# Se eu desejar pegar o inicio até certo ponto, não preciso colocar que ira começar com 0
novaString = texto[:6] 
print(novaString)

# E se eu quiser pegar de um determinado ponto ao final pode ser assim também.
novaString = texto[7:] 
print(novaString)

# Utilizando Step
novaString2 = texto[0:6:2] #Estou dizendo para começar no 0: ir até o caracter 5: e pular de 2 em dois. 
print(novaString2)