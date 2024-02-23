from random import randint
computador = randint(0, 5)
print('-=-' * 15)
print('     Pensando em um numero entre 0 e 5...      ')
print('-=-' * 15)
n = int(input('Digite um numero entre 0 e 5: '))
if n == computador:
    print('Parabens, Voce venceu o computador!')
else:
    print('Voce perdeu! Boa sorte na proxima!')
