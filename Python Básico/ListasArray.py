# Listas/Array em Python

""" 
fatiamento
append: Inserir um valor no final, 
insert: inserir um valor no começo ou em qualquer lugar,
pop: Remover o último elemento da lista, 
del: Deletar um elemento ou uma fatia de elemento da lista,
clear: Limpar a lista, 
extend: Juntar duas listas., + min, max, range
"""
Índices 0     1    2    3    4
lista = ['A', 'B', 'C', 'D', 'E']
       -5  - 4   -3   -2   -1   

print(lista[1])


# Se eu desejar modifcar qualquer elemento do meu array: 
lista[4] = 'Qualquer coisa'
print(lista[4])


# Array também suporta fatiamento:
print(lista[0:5:1])

print(lista[0:3]) # Vai me mostrar somente os 3 primeiros elementos / Lembrando que ele sempre para um número antes do que nós colocamos, por conta do 0

# Podemos omitir o 0 também
print(lista[:3])

# Ou pegar somente o índice dois até o final da lista: 
print(lista[2:])

# Achar o último elemento da minha lista/array: 
print(lista[-1])

Pular de 2 em dois:
print(lista[::2])

Mostrar de forma invertida: 
print(lista[::-1])

list = [1,2,3]
list2 = [4,5,6]
list3 = list + list2  #Aqui estou concatenando as duas lsitas. 
print(list)
print(list2)
print(list3)

Porém, para concatenar, poderiamos fazer esta função: extend() 
list1 = [1,2,3]
list2 = [4,5,6]
list1.extend(list2)  #Com essa função, a lista 2 começa a fazer parte da lista 1 agora.

print(list1)
print(list2)

Função append('') Serve para adicionarmos um valor no final da lista. 
list1 = [1,2,3]
list2 = [4,5,6]
list2.append('Ola!')

print(list1)
print(list2)

Função Insert() Eu posso adicinar um valor em qualquer parte do meu array que eu escolher.
list1 = [1,2,3]
list2 = [4,5,6]
list2.insert(0, 'Coloquei')

print(list1)
print(list2)

# Função pop: Remove o último elemento do array
list1 = [1,2,3]
list2 = [4,5,6]
list2.pop()

print(list1)
print(list2)

# Função del: Deleta um elemnto do array
list1 = [1,2,3,4,5,6]
list2 = [7,8,9,10,11]
del(list2[1:4])

print(list1)
print(list2)

Nós podemos também pegar o valor máximo e minímo da nossa lista.
list1 = [1,2,3,4,5,6]
list2 = [7,8,9,10,11]

print(max(list1))
print(min(list1))

Função list: me retorna todos os valores que eu pedir.
l2 = list(range(1,10))
print(l2)

Soma de todos os valores
list = [0,1,2,3,4,5,6,7,8,9]
soma = 0
for valor in list:
    soma += valor 
print(soma)

Checando cada elemento do meu array.
list = ['String',True, 10, -20.5]
for elem in list:
    print(f'O tipo de {elem} e seu valor é: {type(elem)}')

Exercício com Tudo que vimos praticamente:
Jogo da forca:

secreto = 'dobby'
letras_digitadas = []
chance = 3

while True: 
    if chance <= 0:
        print('Um Dementador pegou você :`)')
        break
    
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Digite apenas uma letra u.u')
        continue
    
    letras_digitadas.append(letra)
    
    if letra in secreto:
        print(f'Uhull, 10 pontos para Grifonória tchê, contém a letra: {letra} \o/')
    else:
        print(f'Eitah` bagual, a letra: {letra}, não contém na palavra secreta. Sinto que tem um Dementador vindo O_O')
        letras_digitadas.pop()
    
    montando_palavra = ''
    for letra_secreta in secreto:
        if letra_secreta in letras_digitadas:
            montando_palavra += letra_secreta
        else:
            montando_palavra += '*'
    
    if montando_palavra == secreto:
        print(f'Expecto patronum -> * * * 100 pontos para Grifnória` você descobriu a palavra secreta:{secreto} e acabou com aqueles Dementadores!!')
        print(f'Parabéns tchê, acabou sua formação em hogwarts u.u')
        break
    else:
        print(f'A palavra secreta está assim: {montando_palavra}')

    if letra not in secreto:
        chance -= 1
    print(f'Você ainda tem: {chance} chances.')
    print()