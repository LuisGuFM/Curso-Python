from random import randint
from time import sleep

print('-='*10, end=(''))
print('JoKenPo', end=(''))
print('-='*10)
print('Vamos jogar!')
print('''Escolha uma opcao: 
      [ 0 ] PEDRA 
      [ 1 ] PAPEL 
      [ 2 ] TESOURA''')
jogador = int(input('Sua escolha: '))
lista = ['PEDRA' , 'PAPEL', 'TESOURA']
maquina = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*10)
print(f'Computador jogou {lista[maquina]}')
print(f'Jogador jogou {lista[jogador]}')
print('-='*10)
if maquina == 0: #MAQUINA ESCOLHEU PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('MAQUINA VENCE!')
    else:
        print('Jogada Invalida!') 
if maquina == 1: #MAQUINA ESCOLHEU PAPEL
    if jogador == 0:
        print('MAQUINA VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('Jogada Invalida!')
if maquina == 2: #MAQUINA ESCOLHEU TESOURA
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('MAQUINA VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada Invalida!')                               