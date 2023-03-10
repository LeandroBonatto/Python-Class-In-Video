num = count = sum = 0
num = int(input('Enter a num [999 to stop]: '))
while num != 999:
     count += 1
     sum = sum + num
     num = int(input('Enter a num [999 to stop]: '))
print('You typed {} numbers and the sum of all was {}.'.format(count, sum))


'''num = cont = soma = 0
num = int(input('Digite um num [999 para parar]: '))
while num != 999:
    cont += 1
    soma = soma + num
    num = int(input('Digite um num [999 para parar]: '))
print('Vc digitou {} numeros e a soma entre todos foi {}.'.format(cont, soma))'''
