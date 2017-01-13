# cria provas com perguntas e repostas em ordem aleatoria, juntamente com os gabaritos contendo as repostas

import random


# os dados para a prova. As chaves sao os estados e os valores as capitais.
capitals = {'Acre': 'Rio Branco', 'Amazonas': 'Manaus', 'Amapa': 'Macapa', 'Roraima': 'Boa Vista',
            'Rondonia': 'Porto Velho', 'Para': 'Belem', 'Tocantins': 'Palmas',
            'Maranhao': 'Sao Luis', 'Piaui': 'Teresina', 'Ceara': 'Fortaleza', 'Rio Grande do Norte': 'Natal',
            'Paraiba': 'Joao Pessoa', 'Pernambuco': 'Recife', 'Alagoas': 'Maceio', 'Sergipe': 'Aracaju',
            'Bahia': 'Salvador',
            'Sao Paulo': 'Sao Paulo', 'Rio de Janeiro': 'Rio de Janeiro', 'Espirito Santo': 'Vitoria',
            'Minas Gerais': 'Belo Horizonte',
            'Mato Grosso do Sul': 'Campo Grande', 'Mato Grosso': 'Cuiaba', 'Goias': 'Goiania',
            'Distrito Federal': 'Brasilia',
            'Parana': 'Curitiba', 'Santa Catarina': 'Florianopolis', 'Rio Grande do Sul': 'Porto Alegre'}

# gera 35 arquivos contendo as provas
for quizNum in range(35):
    # cria os arquivos com as provas e os gabaritos das repostas
    quizFile = open('capitalsqui%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # escreve o cabecalho
    quizFile.write('Nome:\n\nData:\n\nSerie:\n\n')
    quizFile.write((' ' * 20) + 'Capitais dos Estados (Prova %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # embaralha a ordem dos estados
    states = list(capitals.keys())
    random.shuffle(states)

    # percorre todos os 27 estados em um loop, criando uma pergunta para cada um
    for questionNum in range(27):
        # obtem respostas corretas e incorretas
        correctAnswers = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswers)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answersOptions = wrongAnswers + [correctAnswers]
        random.shuffle(answersOptions)

        # grava a pergunta e as opcoes de resposta no arquivo da prova
        quizFile.write('%s. Qual é a capital do estado de(o, a) %s?\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answersOptions[i]))
        quizFile.write('\n')

        # grava o gabarito com as respostas em um arquivo
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answersOptions.index(correctAnswers)]))

    quizFile.close()
    answerKeyFile.close()