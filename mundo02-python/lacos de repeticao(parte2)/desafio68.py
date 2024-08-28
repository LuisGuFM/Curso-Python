from random import randint
v = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    total = jogador + computador
    resp = ' '
    while resp not in 'PI':
        resp = str(input('PAR OU ÍMPAR[P/I]? ').strip().upper()[0])
    print(f'Você jogou {jogador} e o computador jogou {computador}, totalizando em {total}')   
    if resp == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break    
    elif resp == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER!!! Você Saiu com {v} vitória(s)!')  
                