print('{:=^40}'.format(' DOLLAR STORE '))
price = float(input('Purchase price: R$ '))
print('''PAYMENT METHODS
[ 1 ] cash/check
[ 2 ] the card view
[3] 2x on card
[ 4 ] 3x or more on the card''')
option = int(input('Choose option? '))
if option == 1:
     total = price - (price * 10 / 100)
elif option == 2:
     total = price - (price * 5 /100)
elif option == 3:
     total = price
     installment = total / 2
     print('Your purchase will be paid in 2 installments of {:.2f} WITHOUT INTEREST'.format(installment))
elif option == 4:
     total = price + (price * 20 / 100)
     totparc = int(input('How many installments? '))
     installment = total / totparc
     print('Your purchase will be paid in {}x of BRL {:.2f} WITH INTEREST'.format(totparc, installment))
else:
     total = price
     print('INVALID payment option. Please try again.')
print('Your purchase of BRL {:.2f} will cost BRL {:.2f} at the end.'.format(price, total))


'''print('{:=^40}'.format(' LOJAS DOLLAR '))
preco = float(input('Preco das compras: R$ '))
print('FORMAS DE PAGAMENTO
[ 1 ] a vista dinheiro/cheque
[ 2 ] a vista cartao
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao')
opcao = int(input('Escolha a opcao? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 /100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra sera parcelada em 2x de R$ {:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra sera parcelada em {}x de R$ {:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preco
    print('OPCAO INVALIDA de pgto. Tente novamente.')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preco, total))'''

