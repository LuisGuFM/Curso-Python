palavras = ('yasuo', 'caixa', 'adedonha', 'guanabara',
            'vayne', 'fon', 'xesquedele', 'python', 'adventista',
            'Deus', 'amor')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
