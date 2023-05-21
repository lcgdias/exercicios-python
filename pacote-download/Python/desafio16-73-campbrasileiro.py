times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians',
         'Flamengo', 'Athletico-PR', 'Atletico-MG', 'Fortaleza',
         'Sao Paulo', 'America-MG', 'Botafogo', 'Santos',
         'Goias', 'Bragantino', 'Coritiba', 'Cuiaba',
         'Ceara SC', 'Atletico-GO', 'Avai', 'Juventude')
print('-=' * 15)
print(f'Lista de times do Brasileirao: {times}')
print('-=' * 15)
print(f'Os 5 primeiros sao: {times[:5]}')
print('-=' * 15)
print(f'Os 4 ultimos sao: {times[16:]}')
print('-=' * 15)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=' * 15)
print(f'O Fortaleza esta na {times.index("Fortaleza") + 1}a posicao.')