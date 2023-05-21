print('*'*20)
print('TERMOS DE UMA PA')
print('*'*20)
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
d = p + 10 * r
finalizar = False
while p != d:
    print('{} '.format(p), end='')
    p += r
while finalizar == False:
    cont = int(input('\nDeseja mostrar mais quantos termos: '))
    if cont != 0:
        d = p + cont * r
        while p != d:
            print('{} '.format(p), end='')
            p += r
    else:
        print('Fim do programa.')
        finalizar == True