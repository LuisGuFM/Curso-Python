vcasa = float(input('Qual e o valor da casa? R$'))
salario = float(input('Qual e o seu salario? R$'))
vano = int(input('Quantos anos de Financiamento??'))
mensalidade = vcasa / (vano * 12 )
testemensalidade = salario * 30 / 100
if mensalidade > testemensalidade:
    print('Transacao Aceita, a mensalidade nao excedeu 30% do seu salario!')
elif mensalidade < testemensalidade:
    print('Transacao Recusada, a mensalidade excedeu 30% do seu salario!')
elif mensalidade == testemensalidade:
    print('Transacao Arriscada, reconsidere antes de continuar!')       