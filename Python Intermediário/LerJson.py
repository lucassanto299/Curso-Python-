""" Arquivo Criado Só Para ler Json """
import json
# with open('abc.json', 'r') as file:
#     d1_json = file.read()  #Criei uma variável só para ler o arquivo json
#     print(d1_json)


""" Agora Eu quero que isso Retorne a ser um Dicionários, pois assim não consegue acessar nenhuma Chave """
with open('abc.json', 'r') as file:
    d1_json = file.read()  #Criei uma variável só para ler o arquivo json
    d1_json = json.loads(d1_json) #Agora ele voltou a ser um dicionário
    
#Só para visualizar:
for k, v in d1_json.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)