count = n = s = 0
while n != 999:
     n = int(input('Enter a number - (999 - Stop): '))
     if n == 999:
         break
     y += n
     count += 1
print(f'You typed {count} values and the sum was {s}.')


'''cont = n = s = 0
while n != 999:
    n = int(input('Digite um numero - (999 - Parar): '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Vc digitou {cont} valores e a soma foi {s}.')'''