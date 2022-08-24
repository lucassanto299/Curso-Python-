""" Levantando Exceções em Python """
""" Relançando uma Exceção """
#Eu quero logar essas exceções que acontecerem a cada vez que minha
# função for usada de maneira incorrerta
# def divide(n1, n2):
#     try:
#         return n1 / n2 
#     except ZeroDivisionError as error:   #Aqui estou jogando o erro dentro da minha variável error
#         print('Log:', error)   #E aqui estou logando esse erro/ demonstrando qual o erro que está acontecendo.
#         raise   #Estou relaçando minha exceção aqui, para poder pega-la fora do escopo da função

# try:
#     print(divide(2,0))
# except ZeroDivisionError as error:
#     print(error)   #Agora consegui pegar o error fora do escopo da função e estou relançando o erro/ capturei ele para poder relançar.



""" Tendo sua Própria Mensagem de error """
#Caso eu queira mandar uma mensagem ou levantar minha prórpia exceção
#Caso alguém utilize essa exceção ou eu mesmo de maneira incorreta
def divide(n1, n2):
    if n2 == 0:
        raise ValueError('n2, não pode ser 0.')   #Sendo bem especifico de qual erro estou levantando de acordo com minha mensagem/ Isso pega até comentário
    return n1 / n2 
#Se eu desejar capturar esse erro
try:
    print(divide(n1=2,n2=0))
except ValueError as error:
    print('Log:',error)
