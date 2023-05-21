maisvelho = ''
ihmv = 0
media = 0
tot = 0
maisnovas = 0
for nis in range(1, 5):
    print('---- {}ª PESSOA ----'.format(nis))
    nome = str(input('Nome: '.format(nis)))
    idade = int(input('Idade: ').format(nis))
    sexo = str(input('Sexo [M/F]: '))
    tot += idade
    if idade > ihmv and sexo == 'M':
        ihmv = idade
        maisvelho = nome
    if idade < 20 and sexo == 'F':
        maisnovas += 1
media = float(tot / 4)
print('A media de idade do grupo eh {:.1f}.'.format(media))
print('O homem mais velho eh {} e ele tem {} anos.'.format(maisvelho, ihmv))
print('Ao todo sao {} mulheres com menos de 20 anos.'.format(maisnovas))

