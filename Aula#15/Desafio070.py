total = totmil = smallest = count = 0
cheap = ''
while True:
     product = str(input('Product Name: '))
     price = float(input('Price: R$ '))
     count += 1
     total += price
     if price > 1000:
         tothmil += 1
     if count == 1: # or price < lowest: else below could be excluded
         smaller = price
         cheap = product
     else:
         if price < lowest:
             smaller = price
             cheap = product
     resp = ' '
     while resp not in 'SN':
         resp = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]
     if resp == 'N':
         break
print('{:-^40}'.format(' END OF PROGRAM '))
print(f'The purchase total was BRL {total:.2f}')
print(f'We have {totmil} product(s) costing more than a thousand reais.')
print(f'The cheapest product was {cheap} and costs R$ {smaller:.2f}')


'''total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preco: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:  # or preco < menor: else abaixo poderia ser excluido
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {totmil} produto(s) custando mais de mil reais.')
print(f'O produto mais barato foi {barato} e custa R$ {menor:.2f}')'''