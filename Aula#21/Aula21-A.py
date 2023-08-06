def teste():
    x = 8 # variavel local - esta dentro do escopo
    print(f'Na funcao teste, n vale {n}')
    print(f'Na funcao teste, x vale {x}')

# Programa Principal
n = 2 # variavel global - esta fora do escopo
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}')