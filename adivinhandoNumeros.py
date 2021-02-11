from random import *

seed()

num = 0
chances = 5

print('''
===============================================================
======================Adivinhando números======================
===============================================================

Você terá 5 chances para adivinhar o número secreto.

''')

dificuldade = input('''
Selecione a dificuldade:
- Fácil: Número de 1 a 10
- Médio: Número de 1 a 50
- Difícil: Número de 1 a 100 (10 chances)

Qual a sua escolha? (f, m, d)

''')

def facil():
    return 11

def medio():
    return 51

def difcil():
    return 101

dificuldade = dificuldade.lower().strip()

if dificuldade == 'f': 
    num = randint(1, facil())

elif dificuldade == 'm':
    num = randint(1, medio())

elif dificuldade == 'd':
    chances = 10
    num = randint(1, difcil())

while True:
    print()
    p = int(input('Seu palpite: '))

    if p == num:
        print(f'Você ganhou!!! O número era {num} e você acertou com {5 -chances} chances perdida(s).')
        break

    if p < num:
        print('O número é maior.')
    
    if p > num:
        print('O número é menor.')

    chances -= 1

    if chances == 0:
        print(f'Você perdeu!!! O número era {num}.')
        break

    print(f'Chances restantes: {chances}')
