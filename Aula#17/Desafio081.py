valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 26)
print(f'Vc digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente sao {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('Valor 5 nao encontrado!')