class Matricula():
    
    def __init__(self):
        self.__aluno = None
        self.__disciplina = None
        self.__data_matricula = None
        self.__data_cancelamento = None


    def altera_aluno(self, aluno):
        if type(aluno) is not Aluno:
            return False

        self.__aluno = aluno
        return True

    def altera_disciplina(self, disciplina):
        if type(disciplina) is not Disciplina:
            return False

        self.__disciplina = disciplina
        return True

    def retorna_aluno(self):    
        Aluno = self.__aluno
        return Aluno

    def retorna_disciplina(self):
        Disciplina = self.__disciplina
        return Disciplina
    


#NAO MOVER ESSE IMPORT CIRCULAR PARA CIMA
from .Aluno import Aluno
from .Disciplina import Disciplina
