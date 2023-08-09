from Desafio108 import moeda108

p = float(input('Digite o preco: R$ '))
print(f'A metade de R$ {moeda108.moeda(p)} eh R$ {moeda108.moeda(moeda108.metade(p))}')
print(f'O dobro de R$ {moeda108.moeda(p)} eh R$ {moeda108.moeda(moeda108.dobro(p))}')
print(f'Aumentando 10%, temos R$ {moeda108.moeda(moeda108.aumentar(p, 10))}')

