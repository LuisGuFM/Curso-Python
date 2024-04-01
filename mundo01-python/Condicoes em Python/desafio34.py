salario = float(input('Qual e o salario do funcionario? R$'))
if salario <= 1250:
    novosalario = salario + (salario * 15 / 100)
else:
    novosalario = salario + (salario * 10 / 100)
print("Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.".format(salario, novosalario))      