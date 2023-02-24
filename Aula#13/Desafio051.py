print('=' * 25)
print(' ' 'TERMS OF A PA')
print('=' * 25)
t = int(input('First term: '))
r = int(input('Reason: '))
tenth = t + (10 - 1) * r
for c in range(t, tenth + r, r):
     print('{}'.format(c), end=' -> ')
print('FINISHED')


'''print('=' * 25)
print(' ' 'TERMOS DE UMA PA')
print('=' * 25)
t = int(input('Primeiro termo: '))
r = int(input('Razao: '))
decimo = t + (10 - 1) * r
for c in range (t, decimo + r, r):
    print('{}'.format(c), end=' -> ')
print('ACABOU')'''