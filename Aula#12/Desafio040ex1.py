grade1 = float(input('First note: '))
grade2 = float(input('Second note: '))
average = (grade1 + grade2) / 2
print('First score is {:.1f} and second score is {:.1f}, the students average is {:.1f}'.format(grade1, grade2, average))
if average >= 5 and average < 7:
     print('The student is in RECOVERY.')

'''nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a media do aluno eh {:.1f}'.format(nota1, nota2, media))
if media >= 5 and media < 7:
    print('O aluno esta em RECUPERACAO.')'''