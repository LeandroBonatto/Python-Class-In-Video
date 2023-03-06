n = 1
even = odd = 0
while n != 0:
     n = int(input('Enter a value or 0 to stop: '))
     if n!= 0:
         if n % 2 == 0:
             even += 1
         else:
             odd += 1
print('You typed {} even numbers and {} odd numbers!'.format(even, odd))


'''n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n!= 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar += 1
print('Voce digitou {} numeros pares e {} numeros impares!'.format(par, impar))'''