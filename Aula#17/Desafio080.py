list = []
for c in range(0, 5):
     n = int(input('Enter a value: '))
     if c == 0 or n > list[-1]:
         list.append(n)
     else:
         pos = 0
         while pos < len(list):
             if n <= list[pos]:
                 list.insert(pos, n)
                 break
             pos += 1
print('-=' * 26)
print(f'The values entered in order were {list}')


'''lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print('-=' * 26)
print(f'Os valores digitados em ordem foram {lista}')'''
