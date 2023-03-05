phrase = str(input('Enter a phrase: ')).strip().upper()
words = phrase.split()
together = ''.join(words)
inverse = together[::-1]
for letter in range(len(together) -1, -1, -1):
     inverse += together[letter]
print('The inverse of {} is {}'.format(together, inverse))
if inverse == together:
     print('We have a palindrome!')
else:
     print('No palindrome!')


'''frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = .join(palavras)
inverso = junto[::-1]
for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} eh {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('Nao eh palindromo!')'''