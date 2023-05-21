sal = int(input('Digite aqui o seu salário: R$'))
aume1 = (sal*15) / 100
aume2 = (sal*10) / 100
if sal <= 1250:
    print('Seu salário agora será de R${}'.format(sal + aume1))
else:
    print('Seu salário agora será de R${}'.format(sal + aume2))