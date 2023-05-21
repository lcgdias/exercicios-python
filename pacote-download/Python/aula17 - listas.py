# Ao contrario das tuplas, as LISTAS sao mutaveis
# tuplas ()
# listas []
# dados = list()
num = [9, 2, 3, 5, 6]
# Inserir elementos
# lista.append(x) = adiciona um elemento no final da lista
# lista.insert(0, x) = adiciona um elemento na posicao 0
num.append(4)
# Apagar elementos
# del lista[3]
# lista.pop(3)
# lista.remove(x) -> os anteriores removem pela posicao, esse remove pelo conteudo

# Organizar elementos
# lista.sort() -> organiza os elementos em ordem numerica e/ou alfabetica
# lista.sort(Reverse=True) -> organiza os elementos ao contrario

# Copia de elementos
# b = a[:] -> copia os elementos e nao linka eles entre si
a = [2, 4, 7, 8]
b = a[:]
b[2] = 6
print(a)
print(b)
print('-'*15)
# Descoberta da posicao de um elemento
for c, v in enumerate(num):
    print(f'Na posicao {c} encontrei o valor {v}!')
print('Fim da lista.')

# Listas compostas (lista dentro de outra lista)
# lista.append(dados[:])
# (dados[:]) -> fatia os elementos da lista anterior e adiciona via append
# print(pessoas[0][0]) -> mostra na tela o valor da posicao 0 dentro da posicao 0 da lista de fora
galera = [['Joao', 19], ['Maria', 19], ['Ana', 24], ['Pablo', 30]]
print(galera[0][0])

# para ter só um dos elementos de dentro das listas basta usar um loop:
for p in galera:
    print(p[0]) #printará só o que tiver nos primeiros elementos, no caso, os nomes