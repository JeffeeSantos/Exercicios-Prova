print('Programa para calcular média de três alunos e mostrar a maior e a menor.')
while True:

    matriz = []

    for i in range(3):
        nome = input("Digite o nome do aluno {}: ".format((i+1)))
        notas = []
        for j in range(4):
            nota = float(input("Digite a nota {} do aluno {}: ".format((j+1), (i+1))))
            notas.append(nota)
        matriz.append([nome, notas])

    for i in range(3):
        nome = matriz[i][0]
        notas = matriz[i][1]
        print("Aluno {}: {} - Notas: {}".format((i+1), nome, notas))

    medias = []

    for i in range(3):
        notas = matriz[i][1]
        media = sum(notas) / len(notas)
        medias.append(media)
        matriz[i].append(media)

    maior_media = max(medias)
    menor_media = min(medias)
    for i in range(3):
        if matriz[i][2] == maior_media:
            nome_maior = matriz[i][0]
        if matriz[i][2] == menor_media:
            nome_menor = matriz[i][0]

    print("\nAluno com maior média: {}".format(nome_maior))
    print("Aluno com menor média: {}".format(nome_menor))

    opcao = input('Deseja continuar S/N?')
    if opcao.lower()=='n':
        break

