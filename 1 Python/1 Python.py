print('Programa para mostrar os pares, ímpares de cinco números e média geral.')

while True:

    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    n3 = float(input('Digite o terceiro número: '))
    n4 = float(input('Digite o quarto número: '))
    n5 = float(input('Digite o quinto número: '))

    soma = (n1 + n2 + n3 + n4 + n5) / 5

    pares = []
    impares = []

    for i in [n1, n2, n3, n4, n5]:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)

    print('Os números pares são: {}'.format (pares))
    print('Os números ímpares são: {}'.format (impares))
    print('A média geral desses números é: [{:.1f}]'.format (soma))

    opcao = input('Deseja continuar (S/N)?')
    if opcao.lower()=='n':
        break
