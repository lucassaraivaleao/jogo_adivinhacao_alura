print('*********************************')
print('Bem vindo ao jogo de Advinhação !')
print('*********************************')

numero_secreto = 42
total_de_tentativas = 3


for rodada in range(1, total_de_tentativas + 1):
    print(f'Tentativa {rodada} de {total_de_tentativas}')
    chute_str = input('Digite o seu número: ')
    print(f'Você digitou {chute_str}')

    acertou = int(chute_str) == numero_secreto
    maior = int(chute_str) > numero_secreto
    menor = int(chute_str) < numero_secreto

    if acertou:
        print('Você acertou !')
        break
    else:
        if maior:
            print('Você errou! O seu chute foi maior do que o número secreto')
        elif menor:
            print('Você errou! O seu chute foi menor do que o número secreto')


print('Fim do jogo')
