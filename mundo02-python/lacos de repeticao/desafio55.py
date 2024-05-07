maior = 0
menor = 0
for p in range(1,5):
    peso = float(input(f'Peso da {p}a pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso apresentado foi {maior}.')
print(f'O menor peso apresentado foi {menor}.')                    