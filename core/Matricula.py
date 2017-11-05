

from Aluno import Aluno
from Disciplina import Disciplina

class Matricula():
    aluno = None
    disciplina = None
    data_matricula = None
    data_cancelamento = None


    def altera_aluno(self, aluno):
        if type(aluno) is not Aluno:
            return False

        self.aluno = aluno
        return True

    def altera_disciplina(self, disciplina):
        if type(disciplina) is not Disciplina:
            return False

        self.disciplina = disciplina
        return True

    def retorna_aluno(self):    
        Aluno = self.aluno
        return Aluno

    def retorna_disciplina(self):
        Disciplina = self.disciplina
        return Disciplina
    


#NAO MOVER ESSE IMPORT CIRCULAR PARA CIMA
