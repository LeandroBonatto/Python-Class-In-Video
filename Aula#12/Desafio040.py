grade1 = float(input('First note: '))
grade2 = float(input('Second note: '))
average = (grade1 + grade2) / 2
print('First grade {:.1f} Second grade {:.1f}, the students average is {:.1f}'.format(grade1, grade2, average))
if 7 > average >= 5:
     print('The student is in RECOVERY.')
elif average < 5:
     print('The student is REPROVED.')
elif average >= 7:
     print('The student is APPROVED.')


'''nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a media do aluno eh {:.1f}'.format(nota1, nota2, media))
if 7 > media >= 5:
    print('O aluno esta em RECUPERACAO.')
elif media < 5:
    print('O aluno esta REPROVADO.')
elif media >= 7:
    print('O aluno esta APROVADO.')'''