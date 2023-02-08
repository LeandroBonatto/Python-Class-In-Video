num = int(input('Enter an integer: '))
print('Choose one of the bases for conversion:'
   '[ 1 ] converter to BINARY'
   '[ 2 ] converter to OCTAL'
   '[ 3 ] converter to HEXADECIMAL')
option = int(input('Your choice: '))
if option == 1:
      print('{} converted to BINARY is equal to {}'.format(num, bin(num)[2:]))
elif option == 2:
      print('{} converted to OCTAL equals {}'.format(num, oct(num)[2:]))
elif option == 3:
      print('{} converted to HEXADECIMAL is equal to {}'.format(num, hex(num)[2:]))
else:
      print('Invalid option. Try again.')


'''num = int(input('Digite um numero inteiro: '))
print(Escolha uma das bases para conversao:
 [ 1 ] converter para BINARIO
 [ 2 ] converter para OCTAL
 [ 3 ] converter para HEXADECIMAL)
opcao = int(input('Sua opcao: '))
if opcao == 1:
    print('{} convertido para BINARIO eh igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL eh igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL eh igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opcao invalida. Tente novamente.')'''