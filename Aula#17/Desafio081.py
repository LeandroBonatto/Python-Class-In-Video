values = []
while True:
     values.append(int(input('Enter a value: ')))
     resp = str(input('Do you want to continue? [Y/N] '))
     if resp in 'Nn':
         break
print('-=' * 26)
print(f'You typed {len(values)} elements.')
values.sort(reverse=True)
print(f'The values in descending order are {values}')
if 5 in values:
     print('The value 5 is part of the list!')
else:
     print('Value 5 not found!')


'''valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 26)
print(f'Vc digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente sao {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('Valor 5 nao encontrado!')'''

