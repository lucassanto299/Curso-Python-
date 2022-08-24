Ex 1

num = input('Digite o número: ')
print(num)

if num.isdigit():
    num = int(num)
    if num % 2 == 0: 
     print(f'{num}, é par')
   
    else:
        print(f'{num}, é impar')
    
else:
    print('Isso não é um número inteiro.')

Ex 2

horaUser = input('Digite seu horario (0-23): ')

if horaUser.isdigit():
    horaUser = int(horaUser)
    
    if horaUser < 0 or horaUser > 23:
        print('Hora tem que estar entre 0-23')
    else:
        if horaUser <= 11:
            print('Bom dia!')
        elif horaUser <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
else:
    print('Por favor, digite um horário entre 0 e 23')


# Ex 3

nome = input('Qual é seu nome: ')

nomeUser = len(nome)

if nomeUser <= 4:
    print(f'Seu nome: {nome}, é muito curto: {nomeUser}')
    
elif nomeUser <=6:
        print(f'Seu nome: {nome}, é normal: {nomeUser}')

else:
    print('Seu nome é muito grande')