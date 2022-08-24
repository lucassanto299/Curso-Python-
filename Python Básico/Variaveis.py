""" Iniciar com letra, pode conter número, separar_, letras minúsculas """

nome = 'Lucas Santos'
idade = 32 
altura = 1.73
peso = 76
imc = (peso / (altura **2))

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc);

# A forma mais usuda de Strings com Variáveis é com: Fstring

print(f'{nome}, tem, {idade}, anos de idade e seu imc é: {imc:.2f}');


# Exercicio
nome = 'Santos'
idade = 27
altura = 1.73
peso = 76
anoAtual = 2022
anoNascimento = anoAtual - idade 
imc = (peso / (altura **2))

print(f'nome: {nome}, idade: {idade}, peso: {peso}, Ano Atual: {anoAtual}, Data de nascimento: {anoNascimento}, imc: {imc:.2f}')