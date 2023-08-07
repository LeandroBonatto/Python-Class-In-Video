try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados que vc digitou.')
except ZeroDivisionError:
    print(f'Nao eh possivel dividir um numero por zero!')
except KeyboardInterrupt:
    print(f'O usuario preferiu nao informar os dados!')
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado eh {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')