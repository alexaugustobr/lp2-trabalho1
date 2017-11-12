
import datetime

class Matricula():
    
    def __init__(self):
        self.__aluno = None
        self.__disciplina = None
        self.__data_matricula = None
        self.__data_cancelamento = None
        self.__data_confirmacao = None

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
        return self.__aluno

    def retorna_disciplina(self):
        return self.__disciplina
    
    def altera_data_cancelamento(self, data_cancelamento):
        if type(data_cancelamento) != datetime.date:
            return False
        
        self.__data_cancelamento = data_cancelamento

    def altera_data_confirmacao(self, data_confirmacao):
        if type(data_confirmacao) != datetime.date:
            return False
        
        self.__data_confirmacao = data_confirmacao

    def retorna_data_confirmacao(self):
        return self.__data_confirmacao

    def retorna_data_cancelamento(self):
        return self.__data_cancelamento

from .Aluno import Aluno
from .Disciplina import Disciplina
