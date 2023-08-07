def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mErro: Por favor, digite um numero real valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\n\033[31mUsuario preferiu nao digitar esse numero.\033[m')
            return 0
        else:
            return n

n1 = leiaFloat('Digite um numero real: ')