#  Como contar Caracteres 

usuario = input('Digite seu usuário: ');
quant_caract = len(usuario);
print(usuario, quant_caract, type(quant_caract));

# Checagem
if quant_caract < 6:
    print('Não foi cadastrado!')
else:
    print('Você foi cadastrado!');


# Somar caracteres
string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(f'A soma da string1 e string2 é: {len(string1+string2)}')