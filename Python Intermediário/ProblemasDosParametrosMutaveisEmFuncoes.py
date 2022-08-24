""" Problemas Dos Parâmetros Mutáveis em Funções """
""" Problemas com Argumentos Pdrão Mutáveis em Funções """

""" Objetos Mutaveis (Só para lembrar)
- Listas
- Dicionários

    Objetos Imutaveis
- Tuplas
- String
- Números
- True
- False
- None
"""

#A ideia desta função é mandar uma lista, se já tiver uma lista de clientes existente, manda para o meu outro parâmetro de lista vazio e uni as duas lista, a lista que eu criar e a lista já existe.
def lista_de_clientes(clientes_iteravel, lista=None):  
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista

clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'])
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])

print(clientes1)
print(clientes2)