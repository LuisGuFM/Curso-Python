nome = str(input('Qual e o seu nome? '))
if nome == 'Luis':
    print('Que belo nome!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Joao':
    print('Seu nome e bem popular no Brasil!')
else:
    print('Seu nome e bem normal...')        
print(f'Tenha um bom dia, {nome}!')