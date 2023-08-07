from uteis import fatorial, dobro   # Pode gerar conflitos com outra biblioteca
                                    # que tenha o mesmo nome como dobro e fatorial
                                    # utilizar somente como na aula22-C - import uteis


num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} eh {fat}')
print(f'O dobro de {num} eh {dobro(num)}')