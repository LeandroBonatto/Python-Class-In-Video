from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('O computador escolheu {}'.format(itens[pc]))
print('''Suas opcoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
jogador = int(input('Qual eh sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-=' * 11)
print('Pc jogou: {}'.format(itens[pc]))
print('Jogador jogou: {}'.format(itens[jogador]))
print('-=' * 11)
if pc == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('PC VENCE')
    else:
        print('JOGADA INVALIDA!')
elif pc == 1: # computador jogou PAPEL
    if jogador == 0:
        print('PC VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif pc == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('PC VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        ('JOGADA INVALIDA')