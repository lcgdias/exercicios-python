c = n = 0
while True:
    print('-'*20)
    n = int(input('Quer ver a tabuada de que valor? '))
    print('-'*20)
    if n > 0:
        for c in range(1, 11):
            print(f'{n} x {c} = {n * c}')
    else:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')