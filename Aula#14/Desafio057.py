gender = str(input('Enter your gender: [W/M] ')).strip().upper()[0]
while gender not in 'WwMn':
     gender = str(input('Invalid data. Please enter your gender: ')).strip().upper()[0]
print('Gender {} successfully registered'.format(gender))

'''sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sex not in 'WwMn':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))'''