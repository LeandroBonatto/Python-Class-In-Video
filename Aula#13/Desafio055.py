biggest = 0
smallest = 0
for p in range(1, 6):
     weight = float(input('Weight of {} person: '.format(p)))
     if p == 1:
         bigger = weight
         smallest = weight
     else:
         if weight > biggest:
             biggest = weight
         if weight < smallest:
             smallest = weight
print('The biggest weight was {}Kg'.format(biggest))
print('The smallest weight was {}Kg'.format(smallest))


'''maior = 0
menor = 0
for p in range (1, 6):
    peso = float(input('Peso da {} pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {}Kg'.format(maior))
print('O menor peso foi de {}Kg'.format(menor))'''