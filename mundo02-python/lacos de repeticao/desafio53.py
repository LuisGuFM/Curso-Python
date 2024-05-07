frase = str(input('Digite uma frase: ').strip().upper())
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} e {inverso}')
if inverso == junto:
    print('Temos um Palindromo!')
else:
    print('Essa frase nao e um Palindromo!')        