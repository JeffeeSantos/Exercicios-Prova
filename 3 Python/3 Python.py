print('Este programa irá calcular a média de quatro notas de um aluno.')

while True:
    nomeAluno = str(input('Qual é o nome do aluno? '))
    n1 = float(input('Primeira nota do aluno: '))
    n2 = float(input('Segunda nota do aluno: '))
    n3 = float(input('Terceira nota do aluno: '))
    n4 = float(input('Quarta nota do aluno: '))
    media = (n1 + n2 + n3 +n4) / 4
    
    if media >=7: 
        situacao = 'Aprovado!'

    else: 
        situacao = 'Reprovado!'

    print('A média do aluno {} é igual a {:.1f}. Situação: {}'.format (nomeAluno, media, situacao))

    opcao = input('Deseja continuar (S/N)?')
    if opcao.lower()=='n':
        break


    