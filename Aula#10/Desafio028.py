from random import randint
pc = randint(0, 5) # Sorteio
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? ')) # Jogador tenta adivinhar
if jogador == pc:
    print('PARABENS! Vc conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no numero {} e nao no {}!'.format(pc, jogador))