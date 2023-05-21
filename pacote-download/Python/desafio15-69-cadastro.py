mais18 = homens = mulheresmenos20 = 0
while True:
    cont = sexo = ' '
    print('-'*20)
    print('CADASTRE UMA PESSOA'[:20])
    print('-'*20)
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-'*20)
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresmenos20 += 1
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        print('===== FIM DO PROGRAMA =====')
        print(f'Total de pessoas com mais de 18 anos: {mais18}')
        print(f'Ao todo temos {homens} homens cadastrados.')
        print(f'E temos {mulheresmenos20} mulheres com menos de 20 anos.')
        break


