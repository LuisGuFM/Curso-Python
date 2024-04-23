peso = float(input('Qual e o seu peso? (Kg)'))
altura = float(input('Qual e a sua altura? (m)'))
imc = peso / (altura ** 2)
print('Seu imc e {:.1f}.'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Acima do peso')
elif 30 <= imc < 40:
    print('Obesidade')    
else:
    print('Obesidade morbida! Procure um auxilio medico!')              