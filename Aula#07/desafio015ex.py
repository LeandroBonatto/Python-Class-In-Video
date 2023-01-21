''' car = float(input('Quantos dias o carro foi alugado: '))
km = float(input('Quantos km percorrido com o carro: '))
aluguel = car * 60
utilizado = km * 0.15
total = (car * 60) + (km * 0.15)
print('Sabendo que o preco pelo aluguel eh 60 por dia e o km custa 0.15')
print('O preco total a pagar sera de R$ {:.2f}, sendo R$ {:.2f} pelo aluguel e mais R$ {:.2f} pelo km percorrido.'.format(total, aluguel, utilizado)) '''

car = float(input('How many days the car was rented: '))
km = float(input('How many km traveled with the car: '))
rent = car * 60
used = km * 0.15
total = (car * 60) + (km * 0.15)
print('Knowing that the price for the rent is 60 per day and the km costs 0.15')
print('The total price to pay will be BRL {:.2f}, being BRL {:.2f} for the rent and another BRL {:.2f} for the km traveled.'.format(total, rent, used ))