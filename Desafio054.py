from datetime import date
current = date.today().year
totmajor = 0
totminor = 0
for person in range(1, 8):
     birth = int(input('What year was {} person born? '.format(person)))
     age = current - birth
     if age >= 21:
         totmajor += 1
     else:
         totminor += 1
print('We have {} people of legal age'.format(totmajor))
print('In other hand, we have {} underage'.format(totminor))


'''from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade'.format(totmenor))'''