from .Pessoa import Pessoa
from .Usuario import Usuario
import datetime

class Aluno(Pessoa,Usuario):
    
    
    def __init__(self):
        Pessoa.__init__(self)
        Usuario.__init__(self)
        self.__sigla_curso = None
        self.__matriculas = []

    def disciplinas_aluno(self):
        nome_disciplinas = []
        for matricula in self.__matriculas:
            nome_disciplinas.append(matricula.retorna_disciplina().retorna_nome())
        return nome_disciplinas

    def matricular(self, matricula):
        if type(matricula) is not Matricula:
            return False
        if matricula.retorna_disciplina().retorna_nome() != None and matricula.retorna_disciplina().retorna_nome() in self.disciplinas_aluno():
            return False

        self.__matriculas.append (matricula)
        return True

    def confirmar_matricula(self, disciplina):
        if type(disciplina) is not Disciplina:
            return False
        
        if disciplina not in self.__matriculas:
            return False

        index_matricula = self.__matriculas.index(disciplina)

        matricula.data_confirmacao = datetime.datetime.now()

        self.__matriculas[index_matricula] = matricula

        return True
        
    
    def cancelar_matricula(self, disciplina):
        if type(disciplina) is not Disciplina:
            return False
        
        if disciplina not in self.__matriculas:
            return False

        index_matricula = self.__matriculas.index(disciplina)

        matricula.data_cancelamento = datetime.datetime.now()

        self.__matriculas[index_matricula] = matricula

        return True
    def __str__(self):
        return self.retorna_nome()

#NAO MOVER ESSE IMPORT CIRCULAR PARA CIMA
from .Disciplina import Disciplina
from .Matricula import Matricula