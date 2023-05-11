numbers = list()
while True:
     n = int(input('Enter a value: '))
     if n not in numbers:
         numbers.append(n)
         print('Value added successfully!')
     else:
         print('Duplicate value! I will not add...')
     r = str(input('Do you want to continue? [Y/N] '))
     if r in 'Nn':
         break
print('-=' * 20)
numbers.sort()
print(f'You typed the values {numbers}')


'''numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor add com sucesso!')
    else:
        print('Valor duplicado! Nao vou add...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 20)
numeros.sort()
print(f'Vc digitou os valores {numeros}')'''