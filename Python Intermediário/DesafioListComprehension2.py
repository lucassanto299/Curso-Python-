""" Resolver com Apenas 1 linha utilizando List Comprehension, somando todos Valores """

# 1 - Forma Sem List Comprehension
# carrinho = []

# carrinho.append('Produto', 20)
# carrinho.append('Produto', 30)
# carrinho.append('Produto', 50)

# total = 0 

# for produto in carrinho:
#     total += produto[1]
# print(total)

# 2 - Forma (Mais Eficiente que a Primeira)
# carrinho = []

# carrinho.append(('Produto', 20))
# carrinho.append(('Produto2', 30))
# carrinho.append(('Produto3', 50))

# total = [] 

# for produto in carrinho:
#     total.append(produto[1])
# print(sum(total))

# 3 - Forma List Comprehension (Forma Correta)
# carrinho = []

# carrinho.append(('Produto', 20))
# carrinho.append(('Produto2', 30))
# carrinho.append(('Produto3', 50))

# total = sum([value[1] for value in carrinho])
# print(total)
