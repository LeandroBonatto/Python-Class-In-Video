num = list()
pairs = list()
odd = list()
while True:
     num.append(int(input('Enter a number: ')))
     resp = str(input('Do you want to continue? [Y/N] '))
     if resp in 'Nn':
         break
print(num)
for i, v in enumerate(num):
     if v % 2 == 0:
         pairs.append(v)
     elif v % 2 == 1:
         odd.append(v)
print('-=' * 30)
print(f'The complete list: {num}')
print(f'The list of pairs: {pairs}')
print(f'The list of odd: {odd}')


'''num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print(num)
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa: {num}')
print(f'A lista de pares: {pares}')
print(f'A lista de impares: {impares}')'''