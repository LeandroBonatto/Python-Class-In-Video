house = float(input('House value: R$ '))
sal = float(input('Buyers Salary: R$ '))
years = int(input('How many years of financing? '))
installment = house / (years * 12)
min = sal * 30 / 100
print('To pay a house of BRL {:.2f} in {} years'.format(house, years), end='')
print('The installment will be R$ {:.2f}'.format(installment))

print('COMPARING has to pay {} and the minimum is {}'.format(installment, min))


'''casa = float(input('Valor da casa: R$ '))
sal = float(input('Salario do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
pres = casa / (anos * 12)
min = sal * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestacao sera de R$ {:.2f}'.format(pres))

print('COMPARANDO tem que pagar {} e o minimo eh de {}'.format(pres, min))'''