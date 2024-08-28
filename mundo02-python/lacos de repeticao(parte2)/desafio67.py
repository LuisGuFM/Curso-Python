cont = m = 0
while True:
    num = int(input('Deseja ver a tabuada de qual número? '))
    print('='*30)
    if num < 0:
        break
    for cont in range(1, 11):
        print(f'{num} x {cont} = {num * cont}')    
    print('='*30)
print('PROGRAMA DE TABUADA ENCERRADO! Volte sempre!')        