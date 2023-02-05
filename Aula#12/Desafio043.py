weight = float(input('What is your weight in kg? '))
alt = float(input('What is your height? '))
bmi = weight / (alt ** 2)
print('This persons BMI is {:.1f}'.format(bmi))
if bmi < 18.5:
     print('You are BELOW normal weight.')
elif bmi < 25:
     print('CONGRATULATIONS, you are in the NORMAL WEIGHT range.')
elif bmi < 30:
     print('You are OVERWEIGHT.')
elif bmi < 40:
     print('Caution! You are OBESITY.')
else:
     print('You have MORBID OBESITY, be careful!')


'''peso = float(input('Qual eh seu peso em kg? '))
alt = float(input('Qual eh a sua altura? '))
imc = peso / (alt ** 2)
print('O IMC dessa pessoa eh de {:.1f}'.format(imc))
if imc < 18.5:
    print('Vc ta ABAIXO DO PESO normal.')
elif imc < 25:
    print('PARABENS, vc ta na faixa de PESO NORMAL.')
elif imc < 30:
    print('Vc ta em SOBREPESO.')
elif imc < 40:
    print('Cuidado! Vc ta em OBESIDADE.')
else:
    print('Vc ta com OBESIDADE MORBIDA, muito cuidado!')'''