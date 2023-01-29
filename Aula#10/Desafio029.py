speed = float(input('What is the speed of the car? '))
if speed > 80:
     print('FINE! You exceeded the speed limit')
     fine = (speed - 80) * 7
     print('You must pay a fine of R$ {:.2f}'.format(fine))
print('Have a nice day! Drive safely!')


'''veloc = float(input('Qual eh a velocidade do carro? '))
if veloc > 80:
    print('MULTADO! Vc excedeu o limite permitido que eh de 80 km/h')
    multa = (veloc - 80) * 7
    print('Vc deve pagar uma multa de R$ {:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')'''
