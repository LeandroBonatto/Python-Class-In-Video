name = str(input('What is your full name: ')).strip()
split = name.split()
print('Your name in capital letters is {}'.format(name.upper()))
print('Your lowercase name is {}'.format(name.lower()))
print('Your name in total has {} letters'.format(len(name) - name.count(' ')))
print('Your name is {} and has {} letters'.format(split[0], len(split[0])))

'''nome = str(input('Qual eh o seu nome completo: ')).strip()
dividido = nome.split()
print('Seu nome em maiusculo eh {}'.format(nome.upper()))
print('Seu nome em minusculo eh {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu nome eh {} e tem {} letras'.format(dividido[0], len(dividido[0])))'''
