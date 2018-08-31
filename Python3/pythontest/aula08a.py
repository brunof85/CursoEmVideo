from math import sqrt, floor, ceil
import random
import emoji
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} é igual a {}'.format(num, ceil(raiz)))
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
n = random.randint(1,10)
print(n)
print(emoji.emojize('Olá, Mundo :earth_americas:', use_aliases=True))