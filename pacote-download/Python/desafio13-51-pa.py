print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
d = p + (10-1) * r
for c in range(p, d+r, r):
    print('{} '.format(c), end=' -> ')
print('ACABOU')