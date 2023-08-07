def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mErro: Por favor, digite um numero inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\n\033[31mUsuario preferiu nao digitar esse numero.\033[m')
            return 0
        else:
            return n

num = leiaInt('Digite um valor: ')
print(f'O valor digitado foi {num}')