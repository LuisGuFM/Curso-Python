print('Gerador de PA')
print('-=' *10)
i =  int(input('Primeiro Termo: '))
pa = int(input('Razão da PA: '))
c = 1
termo = i
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print(f'{termo} ->', end='')
        termo += pa
        c += 1
        print(' PAUSA')
        mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')    