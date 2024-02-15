dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pagdias = 60 * dias
pagkm = 0.15 * km
pagtotal = pagdias + pagkm
print('O total a pagar e R${:.2f}.'.format(pagtotal))