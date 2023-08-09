import moeda

p = float(input('Digite o preco: R$ '))
print(f'A metade de R$ {p:.2f} eh R$ {moeda.metade(p):.2f}')
print(f'O dobro de R$ {p:.2f} eh R$ {moeda.dobro(p):.2f}')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(p, 10)}')