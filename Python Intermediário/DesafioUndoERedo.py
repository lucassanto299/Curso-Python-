""" Desafio Undo e Redo """
""" 
Faça uma lista de tarefas com as seguintes opções:
adicionar tarefa
listar tarefas
opções de desfazer (A cada vez que chamarmos, desfaz a última ação)
opções de refazer (A cada vez que chamarmos, refaz a última ação)
"""

""" Programa que Adiciona Tarefas, Mas que eu possa Andar para atrás quantas vezes eu desejar e para frente também """
def show_op(todo_list):
    print()
    print('Tarefas: ')
    print(todo_list)
    print()



def do_undo(todo_list, redo_list):    #Eu tenho que checar se tem alguma coisa para eu desfazer
    if not todo_list:
        print('Nada a Desfazer')
        return 
    
    last_todo = todo_list.pop()   #Vai remover o último elemento da lista que é a todo_list, e não apenas issos. Pois ele retorna o valor e vai salvar o valor na variável last_todo  (Resumo: Estou removendo da lista principal e jogando na lista de redo_list, que é de desfazer)
    redo_list.append(last_todo)



def do_redo(todo_list, redo_list):  #E este será o inverso da undo
    if not redo_list:         #Se não tem nada a refazer
        print('Nada a refazer')
        return
    last_redo = redo_list.pop()
    todo_list.append(last_redo)


def do_add(todo, todo_list):
    todo_list.append(todo)




if __name__ == '__main__':
    todo_list = []
    redo_list = []
    

    while True:
        todo = input('Digite Uma Tarefa ou Undo, redo, ls:  ')

        if todo == 'ls':
            show_op(todo_list)
            continue
        elif todo == 'undo':
            do_undo(todo_list, redo_list)  #Assim que eu fizer um desfazer, eu tenho que tirar da minha lista principal que é a todo_list, a ultima coisa que o usuário fez, só que para restaurar isso depois, eu vou ter que jogar na redo_list
            continue
        elif todo == 'redo':
            do_redo(todo_list, redo_list)  #E assim que o usuário falar refazer que é redo, eu vou pegar o que estiver na minha redo_list e vou jogar de volta na minha todo_list, removendo isso da minha redo list, ou seja uma função do undo, é o inverso da redo
            continue

        do_add(todo, todo_list)  #Se não for nenhum comando anterior, o usuário estara adicionando uma tarefa na lista todo_list


