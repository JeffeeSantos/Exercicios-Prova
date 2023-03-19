print('Programa que mostra o número maior e o menor de cinco números.')
while True:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    n3 = float(input('Digite o terceiro número: '))
    n4 = float(input('Digite o quarto número: '))
    n5 = float(input('Digite o quinto número: '))


    maior = max(n1, n2, n3, n4, n5)
    menor = min(n1, n2, n3, n4, n5)


    print('O maior número é: ', maior)
    print('O menor número é: ', menor)

    opcao = input('Deseja continuar (S/N)? ')

    if opcao.lower() == 'n':
        break
