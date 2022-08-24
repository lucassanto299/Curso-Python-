""" Como Criar Módulos em Python """
""" 
Geralmente quando você começa a desenvolver seu programa em python
Geralmente um programa que faço algo até simples, pode ficar Gigante.
Por conta disto, é uma boa prática de programação: Você criar seu programa Organizado
ex:
- Funções que trabalham na Base de Dados: Vão para o Módulo específico que vão para essas funções que trabalham para Base de Dados
- Funções que fazem cálculos: Vão para o Módulo específico de funções que fazem Cálculo
E desta forma você vai quebrando/Modularizando seu programa em Python em arquivos diferentes ou até mesmo em pacotes
"""
# Ex: Digamos que esse arquivo que estamos sirva para fazer cálculos


""" Este arquivo será apenas um Módulo de Cálculo (Assim eu posso usar em outras partes do Programa)"""
import math   #Crei o módulo Math, para saber o valor de PI
PI = math.pi    #Para isso crio uma "Constante", No python, não temos o conceito de constantes, portanto se você quer criar uma constante: Uma variável que não muda seu valor, basta utilizar o Nome da variável em Maiúsculo

def dobra_lista(lista):
    return [value * 2 for value in lista]

def multiplica(lista):
    r = 1  # Por que se fosse 0 alguma coisa iria dar 0, por isso meu R começa com 1
    for value in lista:
        r *= value  
    return r



# Eu faço isso se o módulo for importado para outro módulo, não irá executar isso.
if __name__ == '__name__':
    lista = [1,2,3,4,5]
    print(dobra_lista(lista))
    print(multiplica(lista))
    print(PI)

