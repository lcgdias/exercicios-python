# Variáveis compostas (ou Tuplas)
# se a variável lanche for composta e dentro dela tiver [1: hamburger; 2: suco; 3: pizza; 4: pudim]
lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim')
# print(lanche[0:2]) -> mostra os elementos 0 e 1 do lanche
print(lanche[1:3])
# print(lanche[1:]) -> mostra os elementos de 1 pra frente
print(lanche[1:])
print(lanche[:2])
# print(lanche[-2] -> volta 2 casas a partir da ultima
print(lanche[-2])
# len(lanche) -> mostra quantos elementos tem nessa variável
print(len(lanche))
#                TUPLAS são IMUTÁVEIS
for comida in lanche:
    print(f'\nEu vou comer {comida}')

#ou

for cont in range(0, len(lanche)):
    print(f'\nEu vou comer {lanche[cont]}')

# sorted mostra na ordem alfabetica:
print(sorted(lanche))

# criando tuplas com numeros:
a = (2, 8, 5)
b = (5, 8, 2, 1)
c = b + a
# a ordem das somas altera os resultados da junção
print(c)
# contando quantos numeros tem na tupla:
print(c.count(9)) # quantos numeros 9 tem nessa tupla?
print(c.index(8)) # em que posição está o 8?

# del(c) -> deleta da memória a tupla