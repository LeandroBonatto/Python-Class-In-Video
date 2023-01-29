a = int(input('First value: '))
b = int(input('Second value: '))
c = int(input('Third value: '))
# Checking who is bigger
bigger = a
if b>a and b>c:
     bigger = b
if c>a and c>b:
     bigger = c

print('The bigger value entered was {}'.format(bigger))


'''a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem eh maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('O maior valor digitado foi {}'.format(maior))'''