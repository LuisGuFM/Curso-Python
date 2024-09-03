total = mais1000 = menor = cont = 0
nomemenor = ' '
print('='*30)
print('        MERCADO DO FOND          ')
print('='*30)
while True:
    prto = str(input('Nome do Produto: '))
    preço = float(input('Preço do Produto: R$'))
    total = total + preço
    cont += 1
    if preço > 1000:
        mais1000 += 1
    if cont == 1 or preço < menor:
        menor = preço
        nomemenor = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar sua compra?[S/N] ').strip().upper()[0])
    if resp == 'N':
        break    
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'Total da Compra: R${total:.2f}')
print(f'Produtos acima de R$1000: {mais1000}') 
print(f'Sua compra mais barata foi um/a {nomemenor}, que custou R${menor}')       
