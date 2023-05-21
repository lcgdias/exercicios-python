print('*'*20)
print('TERMOS DE UMA PA')
print('*'*20)
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
d = p + 10 * r
while p != d:
    print('{} '.format(p), end='')
    p += r