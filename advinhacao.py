print('*********************************')
print('Bem vindo ao jogo de Advinhação !')
print('*********************************')

numero_secreto = 42
chute_str = input('Digite o seu número: ')
print(f'Você digitou {chute_str}')

if numero_secreto == int(chute_str):
    print('Você acertou !')
else:
    print('Você errou !')
print('Fim do jogo')