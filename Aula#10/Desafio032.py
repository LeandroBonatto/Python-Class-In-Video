from datetime import date
year = int(input('Which year do you want to analyze? Put 0 to analyze the current year: '))
if year == 0:
     year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
     print('The year of {} is LEAP'.format(year))
else:
     print('The year of {} is NOT LEAP'.format(year))

'''ano = int(input('Qual ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} eh BISSEXTO'.format(ano))
else:
    print('O ano de {} NAO eh BISSEXTO'.format(ano))'''