listagem = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15,
            'Estojo', 20,
            'Bolsa', 50,
            'Apontador', 3,
            'Caneta', 2,
            'Opala v6', 10000,
            'Celta 2001', 2000)
print('-'*40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')    
print('-'*40)
