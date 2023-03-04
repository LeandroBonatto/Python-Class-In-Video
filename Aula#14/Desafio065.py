resp = 'S'
sum = quantity = average = biggest = smallest = 0
while resp in 'Ss':
     num = int(input('Enter a number: '))
     sum += num
     quantity += 1
     if quantity == 1:
         biggest = smallest = num
     else:
         if num > biggest:
             biggest = num
         if num < smallest:
             smallest = num
     resp = str(input('Do you want to continue? [Y/N] ')).upper().strip()[0]
average = sum / quantity
print('You typed {} numbers and the average was {}'.format(quantity, average))
print('The largest value was {} and the smallest was {}'.format(biggest, smallest))


'''resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Voce digitou {} numeros e a media foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))'''