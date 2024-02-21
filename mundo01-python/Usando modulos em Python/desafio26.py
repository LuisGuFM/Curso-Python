frase = input('Escreva uma frase bonita: ').upper().strip()
print(f'A letra A aparace {frase.count('A')}')
print(f'A primeira letra A apareceu na posicao {frase.find('A')+1}')
print(f'A ultima letra A apareceu na posicao {frase.rfind('A')+1}')