""" Trocando valor de Varialvel em Python """
# Sem precisar criar novas variáveis
x = 10
y = 'Santos'

""" forma normal antiga de resolver isso """
z = x 
x = y 
y = z 

print(f'x= {x}, e y={y}')

""" Formal atual """
x, y = y, x   # Para x e y, x recebe y e y esta recebendo x 

print(x, y)

