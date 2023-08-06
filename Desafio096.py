def area(larg, comp):
    a = larg * comp
    print(f'A area de um terreno {larg}x{comp} eh de {a}m2')

print('-' * 30)
print('   CONTROLE DE TERRENOS  ')
print('-' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)