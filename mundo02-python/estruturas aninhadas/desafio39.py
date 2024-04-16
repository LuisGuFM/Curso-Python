from datetime import date
anonascimento = int(input('Em que ano voce nasceu? '))
ano = date.today().year
idade = ano - anonascimento
tempoalistamento = idade - 18
if idade < 18:
    print(f'Voce esta com {idade} anos, ainda faltam {-tempoalistamento} ano/s para voce se alistar!')
elif idade == 18: 
    print(f'Voce esta com {idade} anos, se aliste pela internet ou compareca a junta militar mais proxima!')
else:
    print(f'Voce esta com {idade} anos, se voce nao se alistou, voce esta {tempoalistamento} ano/s atrasado!!')        