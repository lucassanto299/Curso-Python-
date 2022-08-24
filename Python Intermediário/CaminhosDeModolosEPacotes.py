""" Caminhos De Modolos e Pacotes em Python """
#Geralmente não usamos assim, você não vai importar do Main, todos seus arquivos e utilizar
#Pois geralmente dentro de um pacote/Módulo, você importa outro Módulo
# from Pacote1.modulo1 import variavel1
# from Pacote2.modolo2 import variavel2

# print(variavel1)
# print(variavel2)

""" Só que um Programa funciona desta Maneira """
from Pacote2.modolo2 import variavel2  # Vai me trazer o Módulo 1, pois esta importado dentro do módulo 2, mesmo que estejam em níveis diferentes

print(variavel2)