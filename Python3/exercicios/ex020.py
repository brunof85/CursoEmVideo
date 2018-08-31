import random
nome1 = input('Digite o nome do 1º aluno: ')
nome2 = input('Digite o nome do 2º aluno: ')
nome3 = input('Digite o nome do 3º aluno: ')
nome4 = input('Digite o nome do 4º aluno: ')
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))