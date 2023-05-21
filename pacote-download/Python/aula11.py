# Formatando texto
# \033[style;text;back;m
# Códigos de style: 0 (none), 1 (negrito), 4 (sublinhado) e 7 (negativo)
# Códigos de text: 30 (branco), 31 (vermelho), 32 (verde), 33 (amarelo), 34 (azul), 35 (violeta), 36 (ciano), 37 (none)
# Códigos de background: 40-47 (mesma sequência dos de text)

print('\033[7;30;45mOla, mundo!\033[m')

a = 5
b = 3
print('Os valores são \033[32m{}\033 e \033[31m{}\033'.format(a, b))

# Criando um banco de cores

nome = 'Lucas'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('Ola! Muito prazer em conhecer voce, {}{}{}'.format(cores['pretoebranco'], nome, ['limpa']))