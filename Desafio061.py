print('PA Generator')
print('-=' * 10)
first = int(input('First term: '))
reason = int(input('AP reason: '))
term = first
count = 1
while count <= 10:
     print('{} -> '.format(term), end='')
     term = term + reason
     count += 1
print('END')


'''print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + razao
    cont += 1
print(' FIM')'''