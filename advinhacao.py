def jogar():
    import random
    print('*********************************')
    print('Bem vindo ao jogo de Advinhação !')
    print('*********************************')

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print('Qual nível de dificuldade? ')
    print(numero_secreto)
    print('(1) Fácil, (2) Médio (3) Difícil')
    nivel = int(input('Defina o nível: '))
    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f'Tentativa {rodada} de {total_de_tentativas}')
        chute_str = input('Digite o seu número: ')
        print(f'Você digitou {chute_str}')

        if int(chute_str) < 1 or int(chute_str) > 100:
            print('Você deve digitar um número entre 1 e 100')
            continue

        acertou = int(chute_str) == numero_secreto
        maior = int(chute_str) > numero_secreto
        menor = int(chute_str) < numero_secreto

        if acertou:
            print(f'Você acertou e fez {pontos} pontos!')
            break
        else:
            if maior:
                print('Você errou! O seu chute foi maior do que o número secreto')
            elif menor:
                print('Você errou! O seu chute foi menor do que o número secreto')
            pontos_perdidos = abs(numero_secreto - int(chute_str))
            pontos -= pontos_perdidos

    print('Fim do jogo')


if __name__ == '__main__':
    jogar()
