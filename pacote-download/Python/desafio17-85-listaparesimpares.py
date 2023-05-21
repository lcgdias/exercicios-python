valor = [[], []]
n = 0
for c in range(1, 4):
    n = int(input(f'Digite um valor na {c}o posicao: '))
    if n % 2 == 0:
        valor[0].append(n)
    if n % 2 == 1:
        valor[1].append(n)
valor[0].sort()
valor[1].sort()
print('-=' * 30)
print(f'Os numeros pares sao: {valor[0]}')
print(f'Os numeros impares sao: {valor[1]}')