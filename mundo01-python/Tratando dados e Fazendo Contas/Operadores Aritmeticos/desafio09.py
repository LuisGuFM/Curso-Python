medida = float(input('Uma distancia em metros: '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('A medida de {}m em cm vale {:.0f}, e em mm vale {:.0f}'.format(medida, cm, mm))
print('Em dm, {} vale {:.0f}'.format(medida, dm))
print('Em dam, {} vale {}'.format(medida, dam))
print('O valor {}m, vale {}hm'.format(medida, hm))
print('O valor {}m, vale {}km'.format(medida, km))