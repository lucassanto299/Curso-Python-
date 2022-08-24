""" Função Def em Python - Return """
def funcao (var):

    print(var)

variavel = funcao('O valor que eu quero')    #Aqui minha variável irá receber um tipo de dado chamado None: Que signica que não tem valor

print(variavel)                            #Pois o valor esta isolado dentor da minha função, não tendo como passarp para a variável


""" Criando uma condição para Mostrar que não tem valor na variável """
if variavel:    #Vai me retornar um valor booleano, pois desta maneira "if variavavel: " estamos verificando se ela é verdadeira, se tem um valor. 

    print(variavel)    #Como ela não tem valor, irá cair direto no meu else. Não esta retornando nenhum valor para a variável

else:                           

    print('Não tem valor')  

""" Agora Retornando um Valor, para jogar na variável """
def funcao (var): #1- Esta função esta recebendo um valor |Obs2:Parâmetro recebendo o valor

    return var     #2- Repassando o valor | Obs3: Retornar o Valor da função. 
    print('Isso não será exibido')  # Isso aqui não será exebido, pois já estamos dizendo o que é para ser retornado da função.

variavel = funcao('Valor que eu quero') #Aqui eu estou atribuindo o valor que esta sendo Retornado da minha função a minha variável
                                        #3- Estou setando este valor aqui, no meu argumento que é passando este valor para o Parâmetro
if variavel:                            #Obs1: Passando valor para o Parâmetro
    
    print(variavel)

else:
    print('Nenhum Valor')

"""  Possibilidades Interessantes com Return """
"""---Vamos criar uma função que faz uma divisão--- """
def divisao(n1,n2):
    
    if n2 > 0:    #Aqui estou fazendo uma condição para verificar se n2 não é 0, pois retorna um erro se for.
        return n1 / n2
    else:
        print('Conta inválida')

resultado = divisao(8,2)
print(resultado)

""" Dois return  """
def divisao(n1,n2):
    
    if n2 == 0:   
        return    #Se n2 for igual a zero, irá sair da minha função e cair na minha condição de if e else
    
    return n1 / n2


resultado = divisao(8,2)

if resultado:    #Se resultado for verdadeira, meu n2 não for 0
    print(resultado)
else:
    print('Conta inválida!')