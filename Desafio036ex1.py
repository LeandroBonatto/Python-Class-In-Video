vhouse = float(input('House value: R$ '))
wage = float(input('Enter your monthly income: R$ '))
pgtoano = float(input('How many years of payment: '))

weekly = (wage * (30 / 100))
installment = (vhouse / (pgtoano * 12))

print('The installment will be in R$ {:.2f} per month.'.format(installment))
if installment <= weekly:
     print('Authorized Loan!')
else:
     print('Loan Denied!')

'''vcasa = float(input('Valor da casa: R$ '))
sal = float(input('Informe seu rendimento mensal: R$ '))
pgtoano = float(input('Quantos anos de pagamento: '))

presmensal = (sal * (30 / 100))
parcela = (vcasa / (pgtoano * 12))

print('A parcela ficara em R$ {:.2f} por mes.'.format(parcela))
if parcela <= presmensal:
    print('Emprestimo Autorizado!')
else:
    print('Emprestimo Negado!')'''