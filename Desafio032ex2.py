year = int(input('Which year do you want to analyze? '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
     print('The year of {} is LEAP'.format(year))
else:
     print('The year of {} is NOT LEAP'.format(year))


'''ano = int(input('Qual ano quer analisar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} eh BISSEXTO'.format(ano))
else:
    print('O ano de {} NAO eh BISSEXTO'.format(ano))'''