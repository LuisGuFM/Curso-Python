sexo = str(input('Informe seu sexo[M/F]: ')).upper()[0] .strip()
while sexo not in 'MF':
    sexo = str(input('Dados invalidos! Informe o sexo novamente[M/F]: ')).strip() .upper()[0]
if sexo == 'M':
    print('Você é Homem!')
else:
    print('Você é Mulher!')        