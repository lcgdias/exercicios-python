n = s = qntd = 0
while True:
    n = int(input('Digite um numero (999 para parar): '))
    if n != 999:
        s += n
        qntd += 1
    else:
        break
print(f'A soma dos {qntd} valores foi {s}')