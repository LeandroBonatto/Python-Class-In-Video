listnum = []
largest = 0
smallest = 0
for c in range(0, 5):
     listnum.append(int(input(f'Enter a value for position {c}: ')))
     if c == 0:
         largest = smallest = listnum[c]
     else:
         if listnum[c] > largest:
             largest = listnum[c]
         if listnum[c] < smallest:
             smallest = listnum[c]
print('=-' * 30)
print(f'You entered the values {listnum}')
print(f'The largest value entered was {largest} in positions ', end='')
for i, v in enumerate(listnum):
     if v == largest:
         print(f'{i}...', end='')
print()
print(f'The smallest value entered was {smallest} in positions ', end='')
for i, v in enumerate(listnum):
     if v == smallest:
         print(f'{i}...', end='')
print()


'''listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posicao {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'Voce digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posicoes ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} nas posicoes ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print()'''