print('Este programa solicita cinco números e mostra o valor da posição três.')

while True:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    n3 = float(input('Digite o terceiro número: '))
    n4 = float(input('Digite o quarto número: '))
    n5 = float(input('Digite o quinto número: '))

    vetor = [n1, n2, n3, n4 ,n5]
    print('O número que está na posição três é:', vetor[2])

    opcao = input("Deseja continuar (S/N)? ")
    if opcao.lower()=='n':
        break
