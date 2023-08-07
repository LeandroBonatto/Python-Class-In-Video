from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} eh {fat}')
print(f'O dobro de {num} eh {numeros.dobro(num)}')