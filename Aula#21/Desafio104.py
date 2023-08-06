def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um numero inteiro valido.\033[m')
        if ok:
            break
    return valor


# Programa principal
n = leiaInt('Digite um numero: ')
print(f'Vc acabou de digitar o numero {n}.')