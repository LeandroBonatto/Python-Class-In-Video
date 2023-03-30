snack = ('Hamburger', 'Juice', 'Pizza', 'Pudding', 'French fries')

for snack:
     print(f'I am going to eat {snack}')

for count in range(0, len(snack)):
     print(f'I am going to eat {snack[count]} at position {count}')

for pos, food in enumerate(snack):
     print(f'I am going to eat {snack} at position {pos}')

print('I ate like hell!')


'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posicao {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')

print('Comi pra caramba!')'''
