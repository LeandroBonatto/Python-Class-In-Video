from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 nao tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratacao: '))
    dados['salario'] = float(input('Salario: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print('-=' * 30)
print(dados)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')