""" Operador Ternário em Python """

""" Forma antiga """
logged_user = False

if logged_user:
    msg = 'Usuário Logado!'
else:
    msg = 'Usuário precisa Logar!'

print(msg)

""" Forma Atual, usando operador ternário """
logged_user = True
# Se eu desejar preferencia por algum valor primeiro posso colocar () primeiro.
msg = 'Usuário Logado!' if logged_user else 'Usuário precisa Logar!'   # Aqui criei uma variável e passei os valores para ela passando já minha condição.

print(msg)

""" Outro Exemplo """
idade = 18 
maiorDeIdade = (idade >=18)

msg = 'Pode acessar' if maiorDeIdade else 'Não pode acessar!'

print(msg)

""" Exemplo mais Completo """
from unicodedata import numeric


idade = input('Qual é a sua idade: ')

if not idade.isnumeric():
    print('Precisa digitar um Número!')
else:
    idade = int(idade)
    maiorDeIdade = (idade >= 18)
    msg = 'Pode acessar!' if maiorDeIdade else 'Precisa ser maior de 18'
    
    print(msg)