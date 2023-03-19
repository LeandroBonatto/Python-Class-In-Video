from random import randint
v = 0
while True:
     player = int(input('Enter a value: '))
     computer = randint(0, 6)
     total = player + computer
     type = ' '
     while type not in 'PI':
         type = str(input('Even or Odd? [P/I] ')).strip().upper()[0]
     print(f'You played {player} and the computer {computer}. Total of {total}. ', end='')
     print('GIVE EVEN!' if total % 2 == 0 else 'GIVE ODD!')
     if type == 'P':
         if total % 2 == 0:
             print('VC WON!')
             v += 1
         else:
             print('YOU LOST!')
             break
     elif type == 'I':
         if total % 2 == 1:
             print('VC WON!')
             v += 1
         else:
             print('YOU LOST!')
             break
     print('Lets play again...')
print(f'GAME OVER! You won {v} time(s).')


'''from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 6)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Vc jogou {jogador} e o computador {computador}. Total de {total}. ', end='')
    print('DEU PAR!' if total % 2 == 0 else 'DEU IMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('VC VENCEU!')
            v += 1
        else:
            print('VC PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VC VENCEU!')
            v += 1
        else:
            print('VC PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Vc venceu {v} vez(es).')'''