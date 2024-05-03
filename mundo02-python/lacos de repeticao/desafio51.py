print('='*25)
print(' 10 TERMOS DE UMA PA ')
print('='*25)
p =  int(input('Digite o Primeiro termo: '))
r = int(input('Digite a razao: '))
decimo = p + (10 - 1) * r
for c in range (p, decimo , r):
    print(c, end=' ')