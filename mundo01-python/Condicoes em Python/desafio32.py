from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 se quiser analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} e BISSEXTO')
else:
    print(f'O ano {ano} nao e BISSEXTO')    