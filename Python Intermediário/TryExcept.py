""" Try e Except (Tratando Exceções) em Python """
""" 
Exceções: 
- São erros que ocorrem dentro do seu código 
- Elas param a execusão do programa
Para eu tratar exceções em Python, eu envolvo meu código em um Bloco Try 
E Executo o código que eu quero(Similar ao If e Else)
except: 
    E ai faço o que eu quiser na exceção
Se você quiser ver todos erros disponiveis possível, basta digitar Error
"""
""" Esse é o Formato mais Simples de Tratar uma Exceção """
# Pois pega qualquer tipo de erro, mas isso Não é uma boa prática de Programação
# try:
#     print(a)   #Tudo que eu executar dentro do Bloco Try, ele vai tentar executar, se gerar algum erro
# except:        #Vai cair no Except
#     print('Deu certo')   #E aqui eu faço oque eu quiser


""" O ideal é ir no Tipo-Erro/Classe, que gerou e fazer assim """
# try: 
#     a = []
#     b = {}
#     print(b[1])
#     print(a[1])  #Iria cair no meu Except Exception, mas fiz um except só para esse erro de indice, que é o correto

# except NameError as erro:   #Esse é o correto, eu vir aqui e dizer o Tipo de Exceção que eu quero tratar e jogar em uma variavel e printar o erro
#     print('Erro Do desenvolvedor, fale com ele `-`. Nome do erro:', erro)

# except (IndexError, KeyError) as erro:   #Adicionei mais um erro junto
#     print('Erro de índice E Chave.')

# # Se ocorrer mais de uma exceção neste local, podemos fazer outro excepet deste tipo: Exception as erro:
# except Exception as erro:
#     print('Ocorreu um Erro Inesperado')

# print('Bora, vida que segue!')


""" Uma outra coisa que pode Ter no seu Bloco é Else """
# O Else irá ser executado sempre que seu Bloco Try for lançado e não gerar nenhuma exceção ou seja, sem erro
# try: 
#     a = {}   #Agora a tem um dicionário vazio, sem erros
# except NameError as erro:   
#     print('Erro Do desenvolvedor, fale com ele `-`. Nome do erro:', erro)

# except (IndexError, KeyError) as erro:   
#     print('Erro de índice E Chave.')


# except Exception as erro:
#     print('Ocorreu um Erro Inesperado')

# else:
#     print('Seu código foi executado com Sucesso!')
#     print(a)

# print('Bora, vida que segue!')


""" Temos também a Finaly """
# #Diferente do Else, ela será executada sempre, mesmo contendo erros no código
# #Pode ser muito útil se você fechar algum arquivo que tenha sido aberto em algumas das Cláusula ou conexão com a base de dados
# try: 
#     # a = 1/0  
#     #Da mesma maneira se não tiver erro
#     a = 1/0
    
# except NameError as erro:   
#     print('Erro Do desenvolvedor, fale com ele `-`. Nome do erro:', erro)

# except (IndexError, KeyError) as erro:   
#     print('Erro de índice E Chave.')


# except Exception as erro:
#     print('Ocorreu um Erro Inesperado')

# else:
#     print('Seu código foi executado com Sucesso!')
#     print(a)

# finally: 
#     a = None   #Agora não irá gerar mais erro na minha variável a
#     # ou
#     a = ''
#     print('Mesmo com erro no Try, continua executando')

# print('Bora, vida que segue!')


""" Podemos Criar também Try except dentro de Try except """
try:
    a= 0
    try:
        a = 1/0
    except:
        print('erro')
except:
    print('isso')