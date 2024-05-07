somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('-'*5, end='')
    print(f'{p}a Pessoa', end='')
    print('-'*5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').strip())
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1        
mediaidade = somaidade / 4
print(f'A media da idade do grupo e de {mediaidade}')
print(f'O Homem mais velho tem {maioridadehomem} anos e seu nome e {nomevelho}.')
print(f'Ao todo, sao {totmulher20} mulheres com menos de 20 anos.')    