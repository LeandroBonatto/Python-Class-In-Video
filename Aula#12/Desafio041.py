from datetime import date
current = date.today().year
birth = int(input('Birth year: '))
age = current - birth
print('The athlete is {} years old.'.format(age))
if age <= 9:
     print('Classification: MIRIM')
elif age <= 14:
     print('MIRIM PLUS')
elif age <= 19:
     print('JUNIOR')
elif age <= 25:
     print('SENIOR')
else:
     print('MASTER')


'''from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificao: MIRIM')
elif idade <= 14:
    print('Classificacao INFANTIL')
elif idade <= 19:
    print('Classificacao JUNIOR')
elif idade <= 25:
    print('Classificacao SENIOR')
else:
    print('Classificacao MASTER')'''