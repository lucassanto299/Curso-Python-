""" Expressão condicional com Operador Or """
# Sem o operador Or
nome = input('Qual o seu nome: ')

if not nome: 
    print('Você precisa digitar o nome!')

else:
    print(f'Seu nome é: {nome}')

""" Utilizando o Operador Or agora """
nome = input('Qual é seu nome: ')  

print(nome or 'Você precisa digitar seu nome!')    #Ele sempre irá parar na primeira que encontrar Verdadeira. 

""" Valores que retornam Falso com Or """
a = 0    # False
b = None    # False
c = False    # False
d = []    # False
e = {}    # False
f = 22    # Verdadeiro
g = 'Santos'    # Verdadeiro

variable = a or b or c or d or e or f or g    #Irá parar sempre na primeira que encontrar sendo como Verdadeira 

print(variable)

#Sem o Operador Or isso aqui ficaria uma loucura 

if a:
    variavel = a 
elif b:
    variavel = b 
   #etc.. 
