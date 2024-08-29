h = maior = mmenor = 0
while True:
    print('='*30)
    print('     Cadastre uma Pessoa      ')
    print('='*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F]: ').strip().upper()[0])
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        mmenor +=1        
    resp = ' '
    while resp not in 'SN':
        print('='*30)
        resp = str(input('Quer continuar? [S/N]').strip().upper()[0])
    if resp == 'N':
        break
print(f'A quantidade de pessoas maiores de idade registradas são de {maior}')
print(f'A quantidade de homens registrados são de {h}')
print(f'A quantidade de mulheres com idade menor que 20 é de {mmenor}')        
