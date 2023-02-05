name = str(input('What is your name? '))
if name == 'Gustavo':
     print('What a beautiful name!')
elif name == 'Peter' or name == 'Maria' or name == 'Paul':
     print('Your name is very popular in Brazil.')
elif name in 'Ana Claudia Jessica Juliana':
     print('Beautiful Female Name')
else:
     print('Your name is pretty normal.')
print('Have a nice day, {}!'.format(name))


'''nome = str(input('Qual eh seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome eh bem popular no Brasil.')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome Feminino')
print('Tenha um bom dia, {}!'.format(nome))'''