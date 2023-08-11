# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

def calcule(operacao, num, num2):
    if operacao == '1':
        return num + num2
    elif operacao == '2':
        return num - num2
    elif operacao == '3':
        return num * num2
    elif operacao == '4':
        if num2 != 0:
            return num / num2
        else:
            return 'Não existe divisão por zero!'
    else:
        return 'Operação inválida!'

operacao = input('Digite um número para escolher a operação:\n [1]Soma\n [2]Subtração\n [3]Multiplicação\n [4]Divisão\nDigite sua opção 1/2/3/4:')
num = int(input('Digite o 1 número da operação: '))
num2 = int(input('Digite o 2 número da operação: '))

print('O resultado final é:',calcule(operacao, num, num2))