""" Exercícios de Funções """
""" 1 Crie uma Função que exibe uma Saudação com os parâmetros saudação e nome """
def saudacao(saudar,nome):

    print(saudar, nome)

saudacao('Olá,','Lucas Santos')

""" 2 Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles """
def soma(v1, v2, v3):

    print(v1 + v2 + v3)

soma(2,2,2)

""" 3 Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex: 10%). 
Retorne (return) o valor do primeiro número somado do aumento do percentual do mesmo. """
def aumento_percentual(valor, percentual):
    
    return valor + (valor * percentual / 100)

resultado = aumento_percentual(50,10)
print(resultado)
resultado = aumento_percentual(100,10)
print(resultado)
resultado = aumento_percentual(10,10)
print(resultado)
resultado = aumento_percentual(15,100)




""" 4 Fizz Buzz - Se parâmetro da função for divisível por 3, retorne fizz, se o parâmetro da função for
divisível por 5, retorne buzz. Se o parâmetro da função for divisível por 5 e por 3, retorne FizzBuzz, caso
contrário, retorne o número inviado.  """

def fizz_buzz(v1):
    if v1 % 3 == 0 and v1 % 5 == 0:        
            
        return f'FizzBuzz, {v1} é divisível por 3 e 5'
    
    if v1 % 3 == 0:
        
        
            return f'Fizz, {v1} é divisível por 3'
    
    if v1 % 5 == 0:
       
        return f'buzz, {v1} é divisível por 5'
    
    return v1
     
from random import randint
for i in range(10):
    aleatorio = randint(0, 100)
    print(fizz_buzz(aleatorio))