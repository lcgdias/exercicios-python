valor = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite o seu salário: R$'))
anos = int(input('Digite a quantidade de anos que pretende pagar: '))
meses = anos * 12
prest = valor / meses
porcent = (sal*30) / 100
if prest > porcent:
    print('Você não pode fazer esse empréstimo...')
else:
    print('Você pode fazer esse empréstimo...')