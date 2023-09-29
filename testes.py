import unittest
import aluno as a
import turma as t


class turmaTest(unittest.TestCase):

    def setUp(self):
        print('Teste', self._testMethodName, 'sendo executado...')
        self.alunos = []

        self.alunos.append(a.Aluno('Fabio', 'Teixeira', 10))
        self.alunos.append(a.Aluno('Fabiano', 'Teixeira', 8))
        self.alunos.append(a.Aluno('Melissa', 'Teixeira', 6))
        self.alunos.append(a.Aluno('Angela', 'Teixeira', 7))

        self.novaTurma = t.Turma()
        self.novaTurma.cadastrarAlunos(self.alunos)

    def tearDown(self):
        print('Teste', self._testMethodName, 'finalizado.')

    def testMaior(self):
        self.assertEqual(10, self.novaTurma.maiorNota.nota,
                         'Erro ao encontrar maior nota')

    def testMenor(self):
        self.assertEqual(6, self.novaTurma.menorNota.nota,
                         'Erro ao encontrar menor nota')

    def testIntervalo(self):
        #Testar se o intervalo de notas está entre 0 e 10.
        for nota in self.novaTurma.notas:
            self.assertTrue(0 <= nota <= 10,
                            'Erro ao validar intervalo de notas.')


if __name__ == "__main__":
    unittest.main()
