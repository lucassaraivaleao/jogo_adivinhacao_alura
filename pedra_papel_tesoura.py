from random import randint
escolhas = ['', 'pedra', 'papel', 'tesoura']

print('***************************************')
print('Bem vindo ao jogo Pedra, Papel, Tesoura')
print('***************************************')

try:
    escolha_jogador = int(input('1 - pedra, 2 - papel, 3 - tesoura: '))
    escolha_jogador_final = escolhas[escolha_jogador]
    escolha_computador = randint(1, 3)
    escolha_computador_final = escolhas[escolha_computador]
    if escolha_jogador < 1:
        print(print('Ei homi, escolha entre 1-3'))

    def jogar(escolha_j, escolha_c):
        if escolha_j == escolha_c:
            print(f'Você: {escolha_j}')
            print(f'Computador: {escolha_c}')
            print('Empate')

        elif (escolha_j == "pedra" and escolha_c == "papel") or (escolha_j == "papel" and escolha_c == "tesoura") or (escolha_j == "tesoura" and escolha_c == "pedra"):
            print(f'Você: {escolha_j}')
            print(f'Computador: {escolha_c}')
            print('COMPUTADOR VENCEU!')

        elif (escolha_j == "pedra" and escolha_c == "tesoura") or (escolha_j == "papel" and escolha_c == "pedra") or (escolha_j == "tesoura" and escolha_c == "papel"):
            print(f'Você: {escolha_j}')
            print(f'Computador: {escolha_c}')
            print('VOCÊ VENCEU !')
    jogar(escolha_jogador_final, escolha_computador_final)
except ValueError:
    print('Entre com um número inteiro entre 1 e 3!')
