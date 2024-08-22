n = s = m = c = maior = menor = 0
r = "S"
while r in 'Ss':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar[S/N]: ') .upper().strip()[0])
    s += n
    c += 1
    if c == 1:
        mair = menor = c
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
m = s / c                                
print(f'Você digitou {c} números, a soma entre eles é de {s} e a média entre eles é de {m}.')
print(f'O maior número entre eles é {maior}, já o menor é {menor}')    
