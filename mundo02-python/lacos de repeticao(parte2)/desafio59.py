from time import sleep
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Numeros
    [ 5 ] Sair do Programa                   ''')
    opcao = int(input('>>>>>>> O que você deseja fazer? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é de {soma}.')
    elif opcao == 2:
        multi = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} resulta em {multi}.')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2}, o maior número é {maior}')        
    elif opcao == 4:
        print('Informe os números novamente...')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Comando invalido! Tente novamente.')
    print('=-=' * 10)
    sleep(1.5)    
print('Fim do Programa!')
