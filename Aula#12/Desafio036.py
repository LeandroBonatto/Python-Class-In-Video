house = float(input('House value: R$ '))
sal = float(input('Buyers Salary: R$ '))
years = int(input('How many years of funding? '))
isntall = house / (years * 12)
min = sal * 30 / 100
print('To pay a house of BRL {:.2f} in {} years'.format(house, years), end='')
print(' the installment will be R$ {:.2f}'.format(isntall))
if pres <= min:
     print('Loan APPROVED!')
else:
     print('Loan DENIED!')


'''casa = float(input('Valor da casa: R$ '))
sal = float(input('Salario do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
pres = casa / (anos * 12)
min = sal * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestacao sera de R$ {:.2f}'.format(pres))
if pres <= min:
    print('Emprestimo APROVADO!')
else:
    print('Emprestimo NEGADO!')'''
