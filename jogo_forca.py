import random
from os import system, name

frutas = ['banana','laranja','abacaxi','maca','acerola', 'tangerina', 'melao', 'mamao', 'carambola', 'limao', 'tomate', 'mexirica', 'jaca', 'amora', 'jabuticaba', 'melancia', 'morango', 'uva', 'pitaya', 'abacate']
cidades = ['rio de janeiro', 'sao paulo', 'curitiba', 'ourinhos', 'jacarezinho', 'santa cruz do rio pardo', 'avare', 'londrina', 'maringa', 'chavantes', 'ipaussu', 'canitar', 'bernardino de campos']
paises = ['brasil', 'argentina', 'portugal', 'canada', 'mexico', 'japao', 'russia', 'china', 'irlanda', 'franca', 'espanha', 'australia', 'estados unidos', 'colombia', 'peru', 'chile', 'uruguai', 'equador']
nomes = ['gabriel', 'eduardo', 'jessica', 'fatima', 'joao', 'roberto', 'maria', 'silvana', 'esdras', 'yasmim', 'kamila', 'layla', 'jean', 'pedro', 'arthur', 'Lucia']

segredo = ''
retorno = ''
letras_corretas = [' ']
letras_erradas = []
chances = 6

def limpa_tela():
	#windows
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')


def palavra_secreta(num):
	global segredo
	
	if num == 1:
		segredo = random.choice(frutas)
	elif num == 2:
		segredo = random.choice(cidades)
	elif num == 3:
		segredo = random.choice(paises)
	else:
		segredo = random.choice(nomes)
	
	return underscore(segredo, letras_corretas)

def underscore(palavra, lista):
	global retorno
	retorno = ''
	
	for letra in palavra:	
		if letra in lista:
			retorno += letra + ' '
		else:
			retorno += '_ '
			
	print (retorno, '\n')
	
def verificaLetra(letra):
	global letras_corretas
	global letras_erradas
	
	if letra in segredo:
		letras_corretas.append(letra)
	else:
		letras_erradas.append(letra)
		
	underscore(segredo, letras_corretas)
	

#mensagem de boas vindas
limpa_tela()
print('Seja bem-vindo ao jogo da forca =)\n')
print('Que tipo de palavra você gostaria de adivinhar?\n 1. Fruta\n 2. Cidade\n 3. Países\n 4. Nomes Próprios\n')

#peço para o usuário escolher o tipo de palavra p/a adivinhar
lista_escolhida = int(input('Digite o número correspondente a lista de sua preferência: '))
#chamo a função que irá sortear a palavra conforme a lista escolhida!
palavra_secreta(lista_escolhida)

while True:
	if all(letra in letras_corretas for letra in segredo) or len(letras_erradas) > chances:
		break
		
	letra = input('\nAdivinhe uma letra: ')
	print('\n')
	verificaLetra(letra)
	print('Letras erradas:', letras_erradas, '\n')
		
#fim
if (all(letra in letras_corretas for letra in segredo)):
	print('Parabéns!')

if (len(letras_erradas) > chances):
	print('Você perdeu! A palavra secreta era:', segredo)

