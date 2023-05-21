vel = int(input('Parado! Digite a velocidade em que você está dirigindo: '))
mul = (vel - 80) * 7
if vel > 80:
    print('Você foi multado por alta velocidade! A sua multa é de: R${}'.format(mul))