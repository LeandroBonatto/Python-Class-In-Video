words =('learn', 'program', 'language', 'python', 'course', 'free',
             'study', 'practice', 'work', 'market', 'programmer', 'future')
for p in words:
     print(f'\nIn the word {p.upper()} we have ', end='')
     for letter in p:
         if letter.lower() in 'aeiou':
             print(letter, end=' ')


'''palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')'''