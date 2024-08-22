num = c = s = 0
num = int(input("Digite um valor[999 PARA PARAR]: "))
while num != 999:
    c += 1
    s += num
    num = int(input("Digite um valor[999 PARA PARAR]: "))
print(f'Você digitou {c} números e a soma entre eles resulta em {s}.')   
 