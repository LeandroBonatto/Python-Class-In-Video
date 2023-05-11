expr = str(input('Enter expression: '))
stack = []
for simb in expr:
     if simb == '(':
         stack.append('(')
     elif simb == ')':
         if len(stack) > 0:
             stack.pop()
         else:
             stack.append(')')
             break
if len(stack) == 0:
     print('Your expression is valid!')
else:
     print('Your expression is invalid!')


'''expr = str(input('Digite a expressao: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressao ta valida!')
else:
    print('Sua expressao ta invalida!')'''