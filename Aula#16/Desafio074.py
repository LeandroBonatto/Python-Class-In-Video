from random import randint
numbers = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('The selected values were: ', end=' ')
for n in numbers:
     print(f'{n} ', end='')
print(f'\nThe highest value drawn was {max(numbers)}')
print(f'The lowest value drawn was {min(numbers)}')


'''from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end=' ')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')'''