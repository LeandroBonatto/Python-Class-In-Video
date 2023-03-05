sum = 0
count = 0
for c in range(1, 7):
     num = int(input('Enter the {} value: '.format(c)))
     if num % 2 == 0:
         sum += num
         count += 1
print('You entered {} EVEN numbers and the sum was {}'.format(count, sum))

'''soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Voce informou {} numeros PARES e a soma foi {}'.format(cont, soma))'''