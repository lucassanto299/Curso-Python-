""" Uso de Try e Except como Condicional """
def converte_numero(valor):  
    try:    #Se for um número inteiro, vai retornar valor
        valor = int(valor)
        return valor
    except ValueError: #Se for um número flutuante
        try:         
            valor = float(valor)
        except ValueError:  #Se não, vai me retornar None, como todo erro de função, retorna None
            pass  

numero = converte_numero(input('Digite um número: '))   #O que o usuário colocar, vai cair para o parâmetro da minha função
if numero is not None:   #Só vai fazer a conta, se não retornar o valor None
    print(numero * 5)
else:
    print('Digite um Número!')