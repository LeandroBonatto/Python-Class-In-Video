salt = float(input('What is the employees salary? '))
if salt <= 1250:
     new = salt + (salt * 15 / 100)
else:
     new = salt + (salt * 10 / 100)
print('Whoever used to earn BRL {:.2f} now earns BRL {:.2f}'.format(salt, new))


'''sal = float(input('Qual eh o salario do funcionario? '))
if sal <= 1250:
    novo = sal + (sal * 15 / 100)
else:
    novo = sal + (sal * 10 / 100)
print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora'.format(sal, novo))'''