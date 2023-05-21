import calendar
ano = int(input('Digite o ano que você quer saber se é bissexto: '))
bis = calendar.isleap(ano)
if bis == True:
    print('Esse ano é bissexto.')
else:
    print('Esse ano não é bissexto.')