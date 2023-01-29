from random import randint
from time import sleep

pc = randint(0, 5) # Raffle
print('-=-' * 20)
print('I will think of a number between 0 and 5. Try to guess...')
print('-=-' * 20)
player = int(input('What number did I think of? ')) # Player tries to guess
print('PROCESSING...')
sleep(2)
if player == pc:
     print('CONGRATULATIONS! You beat me!')
else:
     print('I WON! I thought number {} and not the {}!'.format(pc, player))


'''pc = randint(0, 5) # Sorteio
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == pc:
    print('PARABENS! Vc conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no numero {} e nao no {}!'.format(pc, jogador))'''