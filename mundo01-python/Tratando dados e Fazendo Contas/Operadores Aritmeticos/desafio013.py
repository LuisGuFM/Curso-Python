produto = float(input('Qual e o valor do produto? R$'))
desconto = produto - (produto * 5 / 100)
input('O produto que custava R${:.2f}, na promocao de 5% vai custar R${:.2f}'.format(produto, desconto))