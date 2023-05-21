lista = par = impar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'A lista completa eh {lista}')
print(f'A lista de pares eh {par}')
print(f'A lista de impares eh {impar}')