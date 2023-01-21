'''
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, o produto vale {} e a divisao vale {:.3}'.format(s, m, d))
print('Divisao inteira {} e potencia {}'.format(di, e))'''

n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('The sum is {}, multiplication is {}, division is {:.2f}'.format(s, m, d))
print('Integer division {} and power {}'.format(di, e))