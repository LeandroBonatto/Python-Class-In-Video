''' aluguel = int(input('Quantos dias alugados? '))
# km = float(input('Quantos km rodados? '))
# total = (aluguel * 60) + (km * 0.15)
# print('O total a pagar eh de R${:.2F}'.format(total)) '''

rent = int(input('How many days rented? '))
km = float(input('How many km driven? '))
total = (rent * 60) + (km * 0.15)
print('Total amount to pay is R${:.2F}'.format(total))
