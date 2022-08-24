""" Desafio Funções 2 """
""" 1 Crie uma função1 que recebe uma função2 como Parâmetro e Retorne o Valor da função2 executada. """
# def ola_mundo():
#     return 'Hi, world!'

# def mestre(funcao):   #Aqui eu criei uma segunda função, retornando o valor dela mesmo
#     return funcao()

# executando = mestre(ola_mundo)    #Aqui eu estou chamando minha segundo função e passando o argumento para ela, que é a minha primeira funcção com o valor dela.
# print(executando)                 # Joguei isso dentro de uma variável e executei esta variável. 



""" 2 Crie uma função1 que Recebe uma função2 como Parâmetro e Retorne o Valor da função2 executada. Faça a função1 executar duas funções que recebam um número diferente de argumentos. """
def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome,saudacao):
    return f'{saudacao} {nome}'

resultado = mestre(fala_oi, 'Lucas Santos')
print(resultado)

resultado2 = mestre(saudacao, 'Lucas Santos', saudacao='Bom dia!')
print(resultado2)