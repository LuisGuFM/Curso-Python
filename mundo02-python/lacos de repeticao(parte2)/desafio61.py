print('Gerador de PA')
print('-='*10)
i = int(input('Primeiro Termo: '))
pa = int(input('Razao da PA: '))
c = 1
termo = i
while c <= 10:
    print(f'{termo} -> ', end='')
    termo += pa
    c += 1
print('FIM')
