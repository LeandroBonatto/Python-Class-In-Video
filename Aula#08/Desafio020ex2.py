from random import shuffle
n1 = str(input('First team: '))
n2 = str(input('Second team: '))
n3 = str(input('Third team: '))
n4 = str(input('Fourth team: '))
n5 = str(input('Fifth team: '))
n6 = str(input('Sixth team: '))
list = [n1, n2, n3, n4, n5, n6]
shuffle(list)
print('The order of presentation will be:')
print(list)

'''n1 = str(input('Primeiro time: '))
n2 = str(input('Segundo time: '))
n3 = str(input('Terceiro time: '))
n4 = str(input('Quarto time: '))
n5 = str(input('Quinto time: '))
n6 = str(input('Sexto time: '))
lista = [n1, n2, n3, n4, n5, n6]
shuffle(lista)
print('A ordem de apresentacao sera:')
print(lista)'''