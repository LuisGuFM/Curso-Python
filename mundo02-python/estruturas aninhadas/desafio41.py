from datetime import date
ano = date.today().year
anonadador = int(input('Em que ano voce nasceu? '))
idade = ano - anonadador
print(f'Voce tem {idade} anos!')
if idade <= 9:
    print('Sua categoria e MIRIM!')
elif  9 < idade <= 14:
    print('Sua categoria e INFANTIL!')
elif 14 < idade <= 19:
    print('Sua categoria e JUNIOR!')
elif 19 < idade <= 25: 
    print('Sua categoria e SENIOR!')
else:
    print('Sua categoria e MASTER!')                 