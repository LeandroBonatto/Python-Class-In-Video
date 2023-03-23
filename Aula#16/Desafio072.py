count = ('zero', 'one', 'two', 'three', 'four',
         'five six seven eight nine',
         'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
         'fifteen', 'sixteen', 'seventeen', 'eighteen',
         'nineteen twenty')
while True:
     num = int(input('Enter a num between 0 and 20: '))
     if 0 <= num <= 20:
         break
     print('Try again. ', end='')
print(f'You typed the number {count[num]}.')


'''cont = ('zero', 'um', 'dois', 'tres', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    num = int(input('Digite um numer entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Vc digitou o numero {cont[num]}.')
'''