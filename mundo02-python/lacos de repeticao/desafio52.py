t = 0
n = int(input('Digite um numero: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end = ' ')
        t += 1
    else:
        print('\033[31m', end = '')    
    print(f'{c}', end=' ')
print(f'\n\033[mO numero {n} foi divisivel {t} vezes.', end = '')
if t == 2:
    print(' Portanto, o numero e PRIMO!')
else:
    print(' Portanto, o numero NAO e PRIMO!')    
