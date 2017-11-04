
from datetime import datetime

class Matricula():
    aluno = None
    disciplina = None
    data_matricula = None
    data_cancelamento = None

    def __init__(self):
        pass

    def altera_aluno(self, aluno):
        if type(aluno) is not Aluno:
            return False

        self.aluno = aluno
        return True


#NAO MOVER ESSE IMPORT CIRCULAR PARA CIMA
from Aluno import Aluno
from Disciplina import Disciplina