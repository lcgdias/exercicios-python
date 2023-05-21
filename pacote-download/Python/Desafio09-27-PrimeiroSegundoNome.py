nome = str(input('Digite o seu nome completo: ')).strip()
sep = nome.split()
print('Primeiro nome: {}'.format(sep[0]))
print('Último nome: {}'.format(sep[len(sep)-1]))