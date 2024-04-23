print('-='*5, end='')
print(' LOJAS FONDZADA ', end='')
print('-='*5)
preco = float(input('Preco das compras: R$'))
print('''FORMAS DE PAGAMENTO
      [ 1 ] a vista em dinheiro ou cheque
      [ 2 ] a vista no cartao
      [ 3 ] em ate 2x no cartao
      [ 4 ] 3x ou mais no cartao''')
opcao = int(input('Qual sera a sua opcao? '))
if opcao == 1:
    novopreco = preco - (preco * 10 / 100)
    print('O valor a ser pago a vista em dinheiro ou cheque sera de R${:.2f}'.format(novopreco))
elif opcao == 2:
    novopreco = preco - (preco * 5 / 100)
    print('O valor a ser pago a vista no cartao sera de R${:.2f}'.format(novopreco))
elif opcao == 3:
    print('O valor a ser pago em ate 2x no cartao sera de R${:.2f}'.format(preco))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparcelas = int(input('Em quantas vezes no cartao? '))
    parcelas = (total / totalparcelas)
    print('Sua compra sera parcelada em {}x de R${:.2f}, totalizando R${:.2f} com juros'.format(totalparcelas, parcelas, total))
else:
    print('Opcao de pagamento incorreta! Tente novamente') 
                     