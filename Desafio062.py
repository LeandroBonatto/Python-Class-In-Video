print('PA Generator')
print('-=' * 10)
first = int(input('First term: '))
reason = int(input('AP reason: '))
term = first
count = 1
total = 0
more = 10
while plus != 0:
     total = total + more
     while count <= total:
         print('{} -> '.format(term), end='')
         term += reason
         count += 1
     print('PAUSE')
     more = int(input('How many terms do you want to show more? '))
print('Progress ended with {} terms shown.'.format(total))


'''print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos vc quer mostrar a mais? '))
print('Progressao finalizada com {} termos mostrados.'.format(total))'''