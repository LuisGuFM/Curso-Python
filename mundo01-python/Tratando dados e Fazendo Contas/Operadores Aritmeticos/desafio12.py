larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensao {}x{} e sua area e de {}m²'.format(larg, alt, area))
tinta = area / 2
print('Para pintar a parede, voce precisara de {}l de tinta'.format(tinta))