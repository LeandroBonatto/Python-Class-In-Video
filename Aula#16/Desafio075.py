num = (int(input('Enter the first number: ')),
     int(input('Enter the second number: ')),
     int(input('Enter the third number: ')),
     int(input('Enter the fourth number: ')))
print(f'You typed the values {num}')
print(f'The value 9 appeared {num.count(9)} time(s)')
if 3 in num:
     print(f'The value 3 appeared in {num.index(3)+1} position')
else:
     print('The value 3 was not entered.')
print('The even values entered were: ', end='')
for n in num:
     if n % 2 == 0:
         print(n, end=' ')


'''num = (int(input('Digite o primeiro numero: ')),
    int(input('Digite o segundo numero: ')),
    int(input('Digite o terceiro numero: ')),
    int(input('Digite o quarto numero: ')))
print(f'Vc digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vez(es)')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1} posicao')
else:
    print('O valor 3 nao foi digitado.')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')'''