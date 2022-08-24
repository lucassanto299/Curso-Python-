""" Escopo de Variáveis em Python """

""" Escopo Global """ 
variavel = 'value'   #Esta variavel esta no escoplo global ou seja, qualquer um pode ter acesso a ela.

def func():
    print(variavel)

""" Isso se Chama escopo Local """
""" ---Você não consegue alterar uma variável Global dentro de uma Função---"""
def func2():
    variavel = 'Outro Valor'   #Aqui é uma nova variavel e não a mesma que esta fora da função, ou seja, estou criando uma nova variavel. Pois ela esta dentro do escopo da função. 
    print(variavel)            # O valor modificado dela só irá aparecer aqui, fora da função, o valor é o mesmo. 

func()
func2()

print(variavel)

""" Mas Se você desejar Alterar o Valor de uma Variável Global Dentro de uma Função """
""" ---NÃo é recomendado fazer Isso, pois pode causar Conflitos---"""
# Preciso dizer que está variavel é globl dentro da minha função, para poder ter acesso a ela e modificala
variavel = 'value'   

def func():
    
    print(variavel)

def func2():
    global variavel    #Aqui estou dizendo que esta variável é global, para poder modificala dentro da função. Se não a função irá simplemente identificar isso como criação de uma variavel qualquer recebendo um valor x. 
    variavel = 'Outro Valor'   
    print(variavel)            

func()
func2()

print(variavel)

""" Mas se eu precisar do Valor da variavel Global e E trabalhar nele, A forma correta é Esta """
variavel = 'value'   

def func():
    
    print(variavel)

def func2(arg=None):
    
    arg = arg.replace('v','c')   
    return arg        

func()
outra_variavel = func2(arg = variavel)

print(outra_variavel)

""" Outros Exemplos """
#Passando o Valor de uma Função para outra
def func():
    
    outra_variavel = 'Lucas Santos'
    return outra_variavel

def func2(arg):
    print(arg)
    
var = func()

func2(var)