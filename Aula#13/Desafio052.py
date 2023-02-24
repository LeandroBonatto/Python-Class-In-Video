num = int(input('Enter a number: '))
total = 0
for c in range(1, num + 1):
     if num % c == 0:
         print('\033[33m', end='')
         total += 1
     else:
         print('\033[31m', end='')
     print('{} '.format(c), end='')
print('\n\033[mThe number {} was divisible {} times!'.format(num, total))
if tot == 2:
     print('And that is why it is PRIME NUMBER')
else:
     print('And that is why it is NOT PRIME NUMBER!')


'''num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisivel {} vezes!'.format(num, tot))
if tot == 2:
    print('E por isso É PRIMO')
else:
    print('E por isso NÃO É PRIMO!')'''