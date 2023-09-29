class Turma:

    def __init__(self):
        self.turma = []
        self.menorNota = None
        self.maiorNota = None
        self.notas = []

    def cadastrarAlunos(self, alunos):
        for aluno in alunos:
            if (0 <= aluno.nota <= 10):
                self.turma.append(aluno)
                self.notas.append(aluno.nota)
                if ((self.menorNota == None)
                        or (self.menorNota.nota > aluno.nota)):
                    self.menorNota = aluno
                if ((self.maiorNota == None)
                        or (self.maiorNota.nota < aluno.nota)):
                    self.maiorNota = aluno
            else:
                print('Alerta: Aluno [', aluno.nome, aluno.sobrenome,
                      '] não cadastrado, nota "', aluno.nota,
                      '" reconhecida como inválida')

    def mostrarAlunos(self):
        print('Quantidade de alunos:', len(self.turma))
        for aluno in self.turma:
            print(aluno.mostrarAluno())

    def mostrarNotas(self):
        print('Notas da turma:')
        for nota in self.notas:
            print(nota)
