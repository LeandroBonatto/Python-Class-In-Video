tot18 = totH = totM20 = 0
while True:
     age = int(input('Age: '))
     sex = ' '
     while sex not in 'MF':
         sex = str(input('Gender: [M/F] ')).strip().upper()[0]
     if age >= 18:
         tot18 += 1
     if sex == 'M':
         totH += 1
     if sex == 'F' and age < 20:
         totM20 += 1
     resp = ' '
     while resp not in 'SN':
         resp = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]
     if resp == 'N':
         break
print(f'Total number of people over 18 years old: {tot18}.')
print(f'In total we have {totH} man(s) registered.')
print(f'And we have {totM20} female(s) under 20.')

'''tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoa(s) com mais de 18 anos: {tot18}.')
print(f'Ao todo temos {totH} homen(s) cadastrados.')
print(f'E temos {totM20} mulher(es) com menos de 20 anos.')'''