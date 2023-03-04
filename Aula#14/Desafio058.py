from random import random
computer = randint(0, 10)
print('I am your computer... I just thought of a number between 0 and 10')
print('Can you guess which one it was? ')
right = False
guesses = 0
while not right:
     player = int(input('Whats your guess? '))
     guesses += 1
     if player == computer:
            right = true
print('Hit with {} attempts!'.format(guesses))


'''from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('Sera que vc consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual eh seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
print('Acertou com {} tentativas!'.format(palpites))'''