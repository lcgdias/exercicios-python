dis = int(input('Digite a distancia (km) da sua viagem: '))
if dis <= 200:
    pas = dis * 0.50
    print('A passagem da sua viagem é R${}'.format(pas))
elif dis > 200:
    pas = dis * 0.45
    print('A passagem da sua viagem é R${}'.format(pas))

# escrevendo de outra forma

dis = int(input('Digite a distancia (km) da sua viagem: '))
preco2 = dis * 0.45
if dis <= 200:
    preco = dis * 0.50
    print('Sua passagem custa R${}'.format(preco))
else:
    print('Sua passagem custa R${}'.format(preco2))