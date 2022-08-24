""" Se eu desejar usar meu Módulo de Cálculo no meu arquivo Appp """
"""  
- from ComoCriarModulos import dobra_lista, multiplica, PI
# Ou
- import ComoCriarModulos
"""

""" Se eu usar desta Maneira """
# import ComoCriarModulos   #Tudo que estiver dentro do Módulo, será executado
# #O problema de usar desta maneira é: Tudo que estiver dentro do Módulo, será executado e trará para o código, mesmo se você selecionar algo específico
# print(ComoCriarModulos.PI)   #Preciso especificar . o que eu quero importar deste Módulo

# Pois se eu usar:
# print(__name__)  #Irei ver que que o nome deste Módulo/Arquivo, ele não se chama app.py, mas sim Main. E o nome do meu Módulo que estou importando para cá, também se chama Main
                #  Por isso acontece o Conflito
# Resumo: Essa variável main que esta sendo executada no meu Módulo Cálculo, ela vai retornar apenas se o módulo estiver sendo importado por outro módulo

#Todo Módulo que esta sendo executado diretamente se chama main, então se você quer testar alguma coisa ou colocar alguma coisa e desejar que ela não seja executada na hora de importar
#Para outro Módulo se usa: if __name__ == '__main__':
#Obs: Em python as pastas são pacotes, onde colocamos os Módulos dentro destas pastas.
""" Se eu usar if __name__ == '__main__':  (Isso não Ocorre) se tiver dentro dó módulo que eu desejo importar"""
# if __name__ == '__name__':
#     print(dobra_lista(lista))
#     print(multiplica(lista))
#     print(PI)

""" Agora eu posso fazer isso, que virá só oque eu selecionar """
# import ComoCriarModulos
# print(ComoCriarModulos.PI)

# lista =[2,4]
# print(ComoCriarModulos.multiplica(lista))

""" Fazendo de Forma Direta """
from ComoCriarModulos import multiplica
print(multiplica([2,4]))