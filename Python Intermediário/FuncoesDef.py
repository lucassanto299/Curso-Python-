""" Funções - Def em Python ( Parte 1 ) """
from mailbox import NotEmptyError


def funcao():    #Sem Parâmetro
    
    print('Hello world!')    #Processamento da minha função

funcao()  #Aqui estou chamando minha função

""" Função também Recebe Parâmetros """
def funcao2 (message):   #Aqui estou atribuindo um Parâmetro/valor, a minha variável chamada funcao2
    
    print(message)     #No processamento, estou dizendo o que é para fazer com meu argumento.

funcao2('Mensagem')    #Chamando Minha função e passando meu argumento para o Parâmetro, dando um valor a ele.

#Resumo: Estou criando um argumento na minha funcão2 
#Depois no processamento, ele irá o mostrar o meu parâmetro.
#E no final estou chamando minha função e passando meu argumento para o parâmetro, que será o valor atribuido a ele.

""" Também não me restrinjo a somente 1 parâmetro """
def saudacao(msg,name):  
    
    print(msg,name)

saudacao('Olá,', 'Lucas Santos')  #Detalhe, sempre quando for passar meu argumento, tem que estar na ordem, de acordo com meu Parâmetro
saudacao('Olá,', 'Jucelino')
saudacao('Olá,', 'Arlequina')
saudacao('Olá,', 'Jurandir')

""" Atribuindo Valores Padrão a uma Função """
def saudacao2(msg='Olá',name='Usuário'):
    
    print(msg,name)

saudacao2()    #Agora este aqui vai receber os valores Padrão que eu passei. Por conta de estar vazio.     
saudacao2('Olá,', 'Lucas Santos') # Aqui estou modificando o Valor padrão do Parâmetro, modificando seu argumento.
saudacao2('Olá,', 'Jucelino')
saudacao2('Olá,', 'Arlequina')
saudacao2('Olá,', 'Jurandir')

""" Alterando a Ordem e os Valores Padrão da Função """
def saudacao3(msg='Olá',name='Usuário'):
    
    print(msg,name)

saudacao3(name='Zezinho', msg='Hi!')    #Aqui eu alterei o valor padrão, mesmo os invertendo. Isso só funcionou porque eu mandei os valores nomeados.     
saudacao3('Olá,', 'Lucas Santos') 
saudacao3('Olá,', 'Jucelino')
saudacao3('Olá,', 'Arlequina')
saudacao3('Olá,', 'Jurandir')

""" Função .replace('', '') """
#Como o próprio nome já diz, substitui algo, por outro.
def saudacao3(msg='Olá',name='Usuário'):
   
    name = name.replace('e', '3')    #Estou dizendo para substituir todas letras 'e' pelo caracter '3' no Parâmetro Name
    msg = msg.replace('e', '3')      #Fazendo a mesma coisa, só que no Parâmetro msg
    print(msg,name)

saudacao3(name='Zezinho', msg='Hi!')    
saudacao3('Olá,', 'Lucas Santos') 
saudacao3('Olá,', 'Jucelino')
saudacao3('Olá,', 'Arlequina')
saudacao3('Olá,', 'Jurandir')

""" Funções Podem e Devem retornar Valores (Forma Certa)"""
def saudacao4(msg='Olá',name='Usuário'):
   
    name = name.replace('e', '3')  
    msg = msg.replace('e', '3')      
    return f'{msg} {name}'   #Aqui Estou dizendo o Valor que é para função me retornar.
 
phrase = saudacao4()   #Atribui o valor da minha função a uma variável 
print(phrase)