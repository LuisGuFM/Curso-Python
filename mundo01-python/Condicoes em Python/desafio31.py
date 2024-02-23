d = float(input('Qual e a distancia da viajem? '))
print('Voce esta prestes a comecar uma viajem de {:.0f}km'.format(d))
if d <= 200:
    total = d * 0.50
else:
    total = d * 0.45    
print('E o preco que voce ira pagar vai ser de R${:.2f}'.format(total))