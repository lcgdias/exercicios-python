ano = int(input('Ano em que nasceu: '))
idade = 2023 - ano
excesso = idade - 18
falta = 18 - idade
if idade <= 17:
    print('Ainda não é hora de se alistar. Faltam {} anos.'.format(falta))
elif idade == 18:
    print('Agora é hora de ir se alistar.')
elif idade > 18:
    print('Já passou da hora de se alistar. Já se passaram {} anos.'.format(excesso))