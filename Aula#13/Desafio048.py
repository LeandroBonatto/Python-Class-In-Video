sum = 0
count = 0
for c in range(1, 501, 2):
     if c % 3 == 0:
         sum += c
         count = count + 1
print('The sum of all {} requested values is {}'.format(count, sum))


'''soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont = cont + 1
print('A soma de todos os {} valores solicitados eh {}'.format(cont, soma))'''