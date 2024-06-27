from random import randint
sorteio = randint(0,10)
print('Sou seu computador...')
print('Acabei de pensar em um número de 0 a 10')
print('Sera que você consegue acertar?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == sorteio:
        acertou = True
    else:
        if jogador < sorteio:
            print('Mais...Tente outra vez')
        else:
            print('Menos...Tente outra vez')       
print(f'Acertou com {palpites} tentativas, Parabéns!')