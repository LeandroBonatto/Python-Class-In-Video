'''# preco = float(input('Qual eh o preco? '))
# desc = preco * 5 / 100
# desconto = preco - desc
# print('O preco do produto eh R$ {}, com desconto fica R$ {:.2f}'.format(preco, desconto))'''

price = float(input('How much is it? '))
clearance = price * 5 / 100
discount = price - clearance
print('The price of the product is BRL {}, with a discount it is BRL {:.2f}'.format(price, discount))