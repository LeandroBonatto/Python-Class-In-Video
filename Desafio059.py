from time import sleep
n1 = int(input('First value: '))
n2 = int(input('Second value: '))
option = 0
while option != 5:
    print('''
    [ 1 ] Add
    [ 2 ] Multiply
    [ 3 ] Major
    [ 4 ] New numbers
    [ 5 ] Exit the program
    ''')
    option = int(input('What is your option? '))
    if option == 1:
        sum = n1 + n2
        print('The sum of {} + {} is {}'.format(n1, n2, sum))
    elif option == 2:
        product = n1 * n2
        print('The result of {} x {} is {}'.format(n1, n2, product))
    elif option == 3:
        if n1 > n2:
            biggest = n1
        else:
            biggest = n2
        print('Between {} and {} the largest value is {}'.format(n1, n2, biggest))
    elif option == 4:
        print('Enter the numbers again.')
        n1 = int(input('First value: '))
        n2 = int(input('Second value: '))
    elif option == 5:
        print('Finishing...')
    else:
        print('Invalid option. Try again.')
    print('=-=' * 10)
    sleep(2)
print('End of program! Check back often!')


'''from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print(
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos numeros
    [ 5 ] Sair do programa
    )
    opcao = int(input('Qual eh a sua opcao? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} eh {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de {} x {} eh {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor eh {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os numeros novamente.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opcao invalida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')'''