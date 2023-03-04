n = int(input('Enter a number to calculate its factorial: '))
c = n
f = 1
print('Calculating {}! = '.format(n), end='')
while c > 0:
     print('{}'.format(c), end='')
     print(' x ' if c > 1 else ' = ', end='')
     f *= c
     c -= 1
print('{}'.format(f))


'''n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))'''
