numeros = []
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Número adicionado!')
    else:
        print('Valor duplicado! Não vou adicionar...')    
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'nN': 
        break
print('-='*30)
numeros.sort()
print(f'Você digitou os valores: {numeros}')    