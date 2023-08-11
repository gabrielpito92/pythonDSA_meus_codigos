# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from os import system, name

frutas = ['banana','laranja','abacaxi','maca','acerola', 'tangerina', 'melao', 'mamao', 'carambola', 'limao', 'tomate', 'mexirica', 'jaca', 'amora', 'jabuticaba', 'melancia', 'morango', 'uva', 'pitaya', 'abacate']
cidades = ['rio de janeiro', 'sao paulo', 'curitiba', 'ourinhos', 'jacarezinho', 'santa cruz do rio pardo', 'avare', 'londrina', 'maringa', 'chavantes', 'ipaussu', 'canitar', 'bernardino de campos']
paises = ['brasil', 'argentina', 'portugal', 'canada', 'mexico', 'japao', 'russia', 'china', 'irlanda', 'franca', 'espanha', 'australia', 'estados unidos', 'colombia', 'peru', 'chile', 'uruguai', 'equador']
nomes = ['gabriel', 'eduardo', 'jessica', 'fatima', 'joao', 'roberto', 'maria', 'silvana', 'esdras', 'yasmim', 'kamila', 'layla', 'jean', 'pedro', 'arthur', 'Lucia']

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

def limpa_tela():
	#windows
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')



# Classe
class Hangman:
	
	# Método Construtor
	def __init__(self, lista):
		self.lista = lista
		self.corretas = [' ']
		self.erradas = []
		self.chances = 5
		self.retornar = ''
		self.letra = ''
		
		if self.lista == 1:
			self.segredo = random.choice(frutas)
		elif self.lista == 2:
			self.segredo = random.choice(cidades)
		elif self.lista == 3:
			self.segredo = random.choice(paises)
		else:
			self.segredo = random.choice(nomes)
		
		self.underscore(self.segredo, self.corretas)
			
	# Método para adivinhar a letra
	def adv_letra(self, letra):
		self.letra = letra
		
		if self.letra in self.segredo:
			self.corretas.append(self.letra)
		else:
			self.erradas.append(self.letra)
			
		self.letra = ''
			
		self.underscore(self.segredo, self.corretas)
	
	# Método para verificar se o jogador venceu
	def verify_win_lose(self):
		if (len(self.erradas) > self.chances):
			print('perdeu')
			print('A palavra secreta era:', self.segredo)
		elif (all(i in self.corretas for i in self.segredo)):
			print('venceu!')
		else:
			self.letra = input('\nAdivinhe uma letra: ')
			self.adv_letra(self.letra)
			
	
	# Método para não mostrar a letra no board
	def underscore(self, segredo, corretas):
		
		self.retornar = ''
	
		for i in self.segredo:	
			if i in self.corretas:
				self.retornar += i + ' '
			else:
				self.retornar += '_ '
		
		self.board(len(self.erradas))
		
		print ('\n', self.retornar, '\n')
		print('Errou:', self.erradas)
		self.verify_win_lose()
		
	def board(self, len_erradas):
		print(board[len_erradas])


#mensagem de boas vindas
limpa_tela()
print('Seja bem-vindo ao jogo da forca =)\n')
print('Que tipo de palavra você gostaria de adivinhar?\n 1. Fruta\n 2. Cidade\n 3. Países\n 4. Nomes Próprios\n')

#peço para o usuário escolher o tipo de palavra p/a adivinhar
lista = int(input('Digite o número correspondente a lista de sua preferência: '))

#init
start = Hangman(lista)
