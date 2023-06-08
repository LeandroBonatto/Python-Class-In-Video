a = [2, 3, 4, 7]
b = a[:] # Se colocar somente b = a (ligacao) se colocar [:] copia de valores.
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
