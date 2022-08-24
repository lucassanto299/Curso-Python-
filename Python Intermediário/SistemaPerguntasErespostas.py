""" Sistema de Perguntas e Respostas com Dicionário """
questions = {
    'Question 1': {
        'Question': 'Quanto é 2 + 2',
        'answers': {
            'a': '6',
            'b': '10',
            'c': '4',
        },
        'answer_secrete': 'c',

    },
    'Question 2': {
        'Question': 'Quanto é 2 * 3',
        'answers': {
            'a': '6',
            'b': '8',
            'c': '16',
        },
        'answer_secrete': 'a',

    },

}
answers_correct = 0
for question_key, question_value in questions.items():
    print(f'{question_key}: {question_value["Question"]}')
    print('Respostas:')

    for answers_key, answers_value in question_value['answers'].items():
        print(f'[{answers_key}]: {answers_value} ')
    
    usuario = input('Sua resposta: ')

    if usuario == question_value['answer_secrete']:
        print('Parabéns!! Você acertou o/')
        answers_correct += 1
    else:
        print('Eitah, você errou :/')

    print()

amounth_questions = len(questions)
percentage = answers_correct / amounth_questions * 100

print(f'Você acertou {answers_correct} respostas!')
print(f'Sua porcentagem de acerto foi {percentage}%')

""" Or """
# if answers_correct == amounth_questions:
#     print(f'Você é Fera mesmo hein, acertou {int(percentage)}%')
# else:
#     print(f'Você acertou {percentage}% :")')