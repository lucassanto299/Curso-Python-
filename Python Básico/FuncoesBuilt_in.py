num1 = input('Digite um número: ');
num2 = input('Digite outro número: ');

# isnumeric isdigit isdecimal
#isnumeric checar se são números e se são positivos.
print(num1.isnumeric())
print(num2.isnumeric())


if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print('Não pode converter os números para realizar contas.')



# Ou Try e Except: Try/tentar se não der certo | Except/excecuto este código aqui
# num1 = input('Digite um número: ');
# num2 = input('Digite outro número: ');

# try:
#     num1= float(num1)
#     num2= float(num2)
#     print(num1 + num2)
# except:
#     print('Erro')