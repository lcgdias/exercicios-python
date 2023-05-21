from random import choice, shuffle
al1 = str(input('Digite o nome do primeiro aluno: '))
al2 = str(input('Digite o nome do segundo aluno: '))
al3 = str(input('Digite o nome do terceiro aluno: '))
al4 = str(input('Digite o nome do quarto aluno: '))
alunos = [al1, al2, al3, al4]
escolhido = choice(alunos)
print('O aluno escolhido foi: {}'. format(escolhido))
