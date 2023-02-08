from datetime import date
current = date.today().year
birth = int(input('Year of birth: '))
age = current - birth
print('Who was born in {} is {} years old in {}.'.format(birth, age, current))
if age == 18:
     print('You must sign up for army IMMEDIATELY!')
elif age < 18:
     balance = 18 - age
     print('Still waiting for {} years to sign up for army'.format(balance))
elif age > 18:
     balance = age - 18
     print('You should have signed up for army {} years ago.'.format(balance))


'''from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Vc tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda fantam {} anos para o alistamento'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Vc ja deveria ter se alistado ha {} anos.'.format(saldo))'''