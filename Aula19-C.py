pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
#pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5  # add sem append
for k, v in pessoas.items():
    print(f'{k} = {v}')