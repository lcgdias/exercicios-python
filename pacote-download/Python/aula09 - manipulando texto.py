# Manipulando cadeias de texto
# A  frase é: Curso em Vídeo Python
# Lembrete: a string começa em 0
frase = 'Curso em Video Python'
print(frase)

# Fatiamento: pegar pedaços de uma string
# frase(9) --> pega a 9ª letra da frase
print(frase[9])
# frase(9:13) --> pega da 9ª até a 12ª letra; o range sempre retira o 1 do último valor
print(frase[9:13])
# frase(9:21:2) --> fatia entre a 9ª e a 21ª letra pulando de 2 em 2 caracteres
print(frase[9:21:2])
# frase(:5) --> pega a 0ª letra até a 4ª letra
print(frase[:5])
# frase(15:) --> fatia a frase da 15ª letra até o final da str
print(frase[15:])
# frase(9::3) --> fatia da 9ª letra até o final da str e pula de 3 em 3 caracteres
print(frase[9::3])

# Análise:
# len(frase) --> length; faz a leitura da quantidade de caracteres
print(len(frase))
# frase.count('o') --> contagem de quantas vezes o caractere 'o' aparece na str
print(frase.count('o'))
# frase.count('o', 0, 13) --> contagem de aparecimento do caractere entre o 0 e o 12
print(frase.count('o', 0, 13))
# frase.find('deo') --> indica em qual posição se encontra o início do 'deo'
print(frase.find('deo'))
# 'Curso' in frase --> retorna valor logico TRUE ou FALSE
print('Curso' in frase)

# Transformação:
# frase.replace('Python', 'Android') --> substitui uma str por outra
print(frase.replace('Python', 'Android'))
# frase.upper(); frase.lower() --> respectivamente, maiúscula & minúscula
print(frase.upper())
print(frase.lower())
# frase.capitalize() --> capitalizar a primeira letra da str
print(frase.capitalize())
# frase.title() --> capitalizar todas as primeiras letras entre espaços (por ex.: Curso Em Vídeo Python)
print(frase.title())
# frase.strip() --> remove os espaços iniciais e finais
# frase.rstrip(); frase.lstrip() ---> remove os espaços da direita e da esquerda, respectivamente

# Divisão:
# frase.split() --> divide uma str em outras str a partir dos espaços colocados, criando uma lista
print(frase.split())
# Junção:
# '-'.join(frase) --> junta as frases da lista dividida; o '-' coloca ao invés de espaço, um - entre as frases