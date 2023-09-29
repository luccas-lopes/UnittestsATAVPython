import aluno as a
import turma as t

alunos = []
alunos.append(a.Aluno('Fabio', 'Teixeira', 8))
alunos.append(a.Aluno('Fabiano', 'Teixeira', 10))
alunos.append(a.Aluno('Melissa', 'Teixeira', -1))

novaTurma = t.Turma()
novaTurma.cadastrarAlunos(alunos)

novaTurma.mostrarAlunos()
novaTurma.mostrarNotas()
print('*' * 30)
print('Aluno com menor nota:', novaTurma.menorNota.mostrarAluno())
print('Aluno com maior nota:', novaTurma.maiorNota.mostrarAluno())
