somaid = 0
mediaid = 0
majoridh = 0
oldname = ''
totwoman20 = 0
for p in range(1, 5):
     print('----- {} PERSON -----'.format(p))
     name = str(input('Name: ')).strip()
     age = int(input('Age: '))
     gender = str(input('Gender [M/F]: ')).strip()
     somaid += age
     if p == 1 and gender in 'Mn':
         majoridh = age
         oldname = name
     if gender in 'Mn' and age > majoridh:
         majoridh = age
         oldname = name
     if gender in 'Ff' and age < 20:
         totwoman20 += 1
mediaid = somaid / 4
print('The average age of the group is {} years'.format(mediaid))
print('The oldest man is {} years old and his name is {}.'.format(majoridh, oldname))
print('A total of {} women under 20'.format(totwoman20))


'''somaid = 0
mediaid = 0
maioridh = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {} PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaid += idade
    if p == 1 and sexo in 'Mn':
        maioridh = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridh:
        maioridh = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaid = somaid / 4
print('A media de idade do grupo eh de {} anos'.format(mediaid))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridh, nomevelho))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(totmulher20))'''