galera = list()
dado = list()
totmaior = totmen = 0
for c in range (0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} eh maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} eh menor de idade')
        totmen += 1

print(f'Temos {totmaior} maior(es) e {totmen} menor(es) de idade.')