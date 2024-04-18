nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2}, a media da materia e de {media}')
if media < 5.0:
    print('Aluno REPROVADO!')
elif 7.0 > media >= 5.0 :
    print('Aluno em RECUPERACAO!')
else:
    print('Aluno APROVADO!')
    