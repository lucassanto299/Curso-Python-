""" Criar um contador  """
""" Usar uma estrutura de repetição While or For """
""" Nessa estrutura de repetição irás criar dois contadores 
    E esse contador que irás criar tem que ser de uma vez só
    Tudo dentro do mesmo laço. 
    Cada volta do laço um contador vai contar de forma progressiva
    Enquanto na segunda irá contar de forma regressiva.
    Enquanto um contador vai ter 0 na primeira volta do laço o outro irá ter 10
0   10
1   9
2   8
3   7
4   6
5   5
6   4
7   3
8   2
9   1
10  0
"""
""" Utilizando While """
progressive = 0
regressive = 10

while progressive <= 10 and regressive >= 1:
    progressive +=1
    print(progressive, end=' ')
    
    regressive -=1
    print(regressive)

""" Utilizando For 'Como um Sênior faria isso..' """
for numberProgressive in range(10):
    print(numberProgressive, end=' ')
    
for numberRegressive in range(10,0,-1):
    print(numberRegressive, end=' ')

