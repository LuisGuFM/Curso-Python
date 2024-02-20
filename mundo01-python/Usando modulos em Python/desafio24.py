cidade = input('Qual e a sua cidade? ')
cidade = cidade.upper()
dividido = cidade.split()
if dividido[0] == 'SANTO' :
    print('Sua cidade comeca com Santo!')
else :
    print('Sua cidade nao comeca com Santo!')   