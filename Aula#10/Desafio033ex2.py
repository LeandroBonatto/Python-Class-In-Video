a = int(input('First value: '))
b = int(input('Second value: '))
c = int(input('Third value: '))
# Checking who is minor
smaller = a
if b<a and b<c:
     smaller = b
if c<a and c<b:
     smaller = c
print('The smallest value entered was {}'.format(smaller))


'''a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem eh menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O menor valor digitado foi {}'.format(menor))'''