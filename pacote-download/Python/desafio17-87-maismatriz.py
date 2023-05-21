matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = ster = mai = 0
for c in range(0, 3):
    for l in range(0, 3):
        matriz[c][l] = int(input(f'Digite um valor na posicao [{c}, {l}]: '))
        if matriz[c][l] % 2 == 0:
            spar += matriz[c][l]
        if matriz[l] == 3:
            ster += matriz[c][l]
        if matriz[c] == 2 > mai:
            mai = matriz[c][l]
print('-=' * 30)
for c in range(0, 3):
    for l in range(0, 3):
        print(f'[ {matriz[c][l]:^5} ]', end='')
    print()
print('-=' * 30)
print(spar)
print(ster)
print(mai)