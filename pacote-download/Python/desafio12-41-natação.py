ano = int(input('Ano em que nasceu: '))
idade = 2023 - ano
if idade <= 9:
    print('Natacao MIRIM.')
elif idade > 9 and idade <= 14:
    print('Natacao INFANTIL.')
elif idade > 14 and idade <= 19:
    print('Natacao JUNIOR.')
elif idade == 20:
    print('Natacao SENIOR.')
elif idade > 20:
    print('Natacao MASTER')