import random


def imprimir_mensagem_de_abertura():
	print('*********************************')
	print('***Bem vindo ao jogo de Forca!***')
	print('*********************************')

def carrega_palavra_secreta():
	arquivo = open('palavras.txt', 'r')
	palavras = []

	for linha in arquivo:
		linha = linha.strip()
		palavras.append(linha)

	arquivo.close()

	numero = random.randrange(0, len(palavras))
	palavra_secreta = palavras[numero].upper()
	return palavra_secreta

def jogar():
	imprimir_mensagem_de_abertura()
	palavra_secreta = carrega_palavra_secreta()
	
	letras_acertadas = ['_' for _ in palavra_secreta]
	# for _ in palavra_secreta:
	#	letras_acertadas.append('_')

	print(letras_acertadas)
	enforcou = False
	acertou = False
	erros = 0

	while not enforcou and not acertou:
		chute = input('Qual letra? ')
		chute = chute.strip().upper()

		if(chute in palavra_secreta):
			index = 0
			for letra in palavra_secreta:
				if chute == letra:
					letras_acertadas[index] = letra
				index += 1
		else:
			erros += 1
		enforcou = erros == 6
		acertou = '_' not in letras_acertadas
		letras_faltando = str(letras_acertadas.count('_'))
		print(f'Ainda faltam acertar {letras_faltando} letras')
		print(letras_acertadas)
	if acertou:
		print('Você ganhou!')
	else:
		print('Você perdeu !')
	print("Fim do Jogo")


if __name__ == '__main__':
	jogar()
