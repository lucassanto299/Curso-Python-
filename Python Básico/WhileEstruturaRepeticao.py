# While em Python
""" 
Utilizado para realizar ações enquanto uma condição for verdadeira.
Em Python temos dois laços para fazer repetições: While e For. 
Nesta, iremos ver o laço While (While Significa: Enquanto..).
"""

while True:  #Aqui ele fara um loop infinito, pois coloquei a condição com valor True já. 
    nome = input('Qual é seu nome: ')
    print(f'Olá, {nome}!')


print('Não vai ser executado')


# Esta condição agora vai até 99, pois depois de 99 é 100
x = 0
while x < 5:  # Aqui estou fazendo a condição, x é amior que 100?
    print(x)  #Aqui estou dando o print do valor de x
    x = x + 1  # Agora estou modificando o valor de x/ ele vai setar uma sona. Toda vez que ele passar por aqui
    # vai somar mais 1 ao meu x, até 100 e quebrar o laço de repetição, caindo no print que fiz logo abaixo fora do while.


print('Acabou!')  #Estou colocando este print fora para quando a condição der falsa,
#  até o 100 ele sai fora do laço de repetição.

# Utilizando a palavra continue. 




x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue 
    print(x)      
    x = x + 1

print('Acabou!')


# Utilizando Break 

x = 0
while x < 10:
    if x == 3:     #Quando aqui o x for = 3 ele caira no nosso break
        x = x + 1   
        break 
    print(x)      
    x = x + 1

print('Acabou!')


# Mais um exemplo

x = 0

while x < 10: 
    y = 0 
    while y < 5:
        print(f'{x},{y}')
        y += 1
    x += 1  # Isso aqui é a mesma coisa: x = x + 1
print('Acabou!')


# Exemplo 3  Calculadora

while True:
    print()
    num = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite um Operador agora: ')
    sair = input('Se desejar sair, digite: Sim[s] ou Não[n] para continuar: ')
     
    if sair == 's':
        break
    elif sair == 'n':
        pass

    if not num.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar um número!')
        continue

    num = int(num)
    num2 = int(num2)
    
    if operador == '+':
        print(num + num2)
    
    elif operador == '-':
        print(num - num2)
    
    elif operador == '/':
        print(num / num2)
    
    elif operador == '*':
        print(num * num2)
    
    else:
        print('Isso não é um Operador')
