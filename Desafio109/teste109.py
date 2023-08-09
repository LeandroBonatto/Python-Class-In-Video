from Desafio109 import moeda109

p = float(input('Digite o preco: R$ '))
print(f'A metade de R$ {moeda109.moeda(p)} eh R$ {moeda109.metade(p, True)}')
print(f'O dobro de R$ {moeda109.moeda(p)} eh R$ {moeda109.dobro(p, True)}')
print(f'Aumentando 10%, temos R$ {moeda109.aumentar(p, 10, True)}')

