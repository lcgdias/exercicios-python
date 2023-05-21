largura = float(input('Digite a largura da parede (m): '))
altura = float(input('Digite a altura da parede (m): '))
area = float(altura * largura)
print('A área dessa parede é de {:.3f}m² e para pintá-la, serão necessários {:.3f}L de tinta.'.format(area, area*2))