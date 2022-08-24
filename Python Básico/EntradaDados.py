#  Entrada de Dados

nome = input('Qual seu nome? ');
idade = input('Qual sua idade? '); 

ano_nascimento = 2022 - int(idade)  #Aqui utilizamos o casting: Que é converter valores. Convertemos uma string para um número inteiro.

print()  #Utilizado vazio desta maneira para gerar uma quebra de linha. 
print(f'Nome: {nome}, e sua idade: {idade}, e o ano de nascimento: {ano_nascimento}')

# Para não precisar converter dentro da nossa saída de dados
# Podemos converter desta forma na Entrada:
nome = int(input('Qual seu nome? '));
idade = int(input('Qual sua idade? ')); 

