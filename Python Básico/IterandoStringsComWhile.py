#       Índices
#       0123456789...............33
frase = 'O rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0 
nova_string = ''
while contador < tamanho_frase:
    print(frase[contador], contador)
    contador += 1


# Agora se eu quiser passar todas as Letras R para maiúsculo da frase: 
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == 'r':
        nova_string += 'R'
    else:
       nova_string += letra
    contador += 1
print(nova_string)


# Agora perguntando para o usuário qual ele deseja:
frase = 'O rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0 
nova_string = ''

usuario = input('Qual letra o senhor(a) deseja que seja maiúscula: ')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == usuario:
        nova_string += usuario.upper()
    else:
        nova_string += letra
    contador +=1
print(nova_string)