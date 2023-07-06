estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())  # usar o [:] para copiar os fatiamentos dos dados da errado. Usar copy.
for e in brasil:
    print(e)