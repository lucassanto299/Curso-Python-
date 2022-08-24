 # Tipos de dados primitivos # 
"""
str - string - textos 'Assim' ou "Assim" 
int - inteiro - 123456 - Númerio inteiro, são números que não tem . numeros com virgulo. Pode ser + ou -
float - real/ponto flutuante - É um número com . ou seja, com "," Pode ser também + ou - 
bool - booleano/lógico - E o valor boleano só tem dois valores: true ou false. Ele é lógico por que checa os valores das coisas. 
Usado geralmente em comparações: Ex true/false 10 == 10 

"""
# Função type serve para verificar a tipagem daquele grupo, de qual ele pertence: 
print('Santos', type('Santos'))
print(10, type(10))
print(25.23, type(25.23))
print(10==10, type(10==10))

# Podemos também fazer conversões de Valores: 
print('10', type('10'), type(int('10')))

# String: nome
print('Santos', type('Santos'))

# Idade: int
print(27, type(27))

# Altura: float
print(1.73, type(1.73))

# É maior de idade:  27 > 18
print(27 > 18, type(27 > 18))