from math import sin, cos, tan, radians
a = float(input('Digite o angulo que voce deseja: '))
sen = sin(radians(a))
print('O angulo {} tem o Seno de {:.2f}'.format(a, sen))
cos = cos(radians(a))
print('O angulo {} tem o Cosseno de {:.2f}'.format(a, cos))
tan = tan(radians(a))
print('O angulo {} tem a Tangente de {:.2f}'.format(a, tan))