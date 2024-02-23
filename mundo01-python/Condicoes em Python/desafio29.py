vel = int(input('Qual e a velocidade atual do carro? '))
if vel <= 80:
    print('Tenha um bom dia! Dirija com seguranca.')
else:
    print('MULTADO! Voce excedeu o limite permitido que e de 80Km/h')
    multa = (vel - 80) * 7
    print('Voce deve pagar uma multa de R${:.2f}'.format(multa))
    print('Tenha um bom dia! Dirija com seguranca.')    