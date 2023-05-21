n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
di = n1 // n2
d = n1 / n2
exp = n1**n2
print('A soma vale {}, \n a divisão vale {:.3f}, \n a divisão inteira vale {} e \n a exponenciação vale {}'.format(s, d, di, exp), end='')