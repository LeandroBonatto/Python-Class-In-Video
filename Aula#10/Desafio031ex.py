dist = float(input('How far is your trip? '))
print('You are about to start a journey of {:.0f} Km.'.format(dist))
if dist <= 200:
     price = dist * 0.50
else:
     price = dist * 0.45
print('And the price of your ticket will be R${:.2f}'.format(price))


'''dist = float(input('Qual a distancia da sua viagem? '))
print('Vc ta prestes a comecar uma viagem de {:.0f} Km.'.format(dist))
if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print('E o preco da sua passagem sera de R${:.2f}'.format(preco))'''
