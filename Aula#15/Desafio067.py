while True:
     n = int(input('Want to see the multiplication table of which value? '))
     if n < 0:
         break
     print('-' * 30)
     for c in range(1, 11):
         print(f'{n} x {c} = {n*c}')
     print('-' * 30)
print('Time tables program terminated. Come back soon!')


'''while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-' * 30)
    for c in range (1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('Programa tabuada encerrado. Volte sempre!')'''