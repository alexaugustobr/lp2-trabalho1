from Pessoa import Pessoa
from Usuario import Usuario
import datetime

class Aluno(Pessoa,Usuario):
    sigla_curso = None
    matriculas = []

    def disciplinas_aluno(self):
        nome_disciplinas = []
        for matricula in self.matriculas:
            nome_disciplinas.append(matricula.disciplina.nome)
        return nome_disciplinas

    def matricular(self, matricula):
        if type(matricula) is not Matricula:
            return False
        if matricula.disciplina.nome != None and matricula.disciplina.nome in self.disciplinas_aluno():
            return False

        self.matriculas.append (matricula)
        return True

    def confirmar_matricular(self, matricula):
        if type(matricula) is not Matricula:
            return False
        
        if matricula not in self.matriculas:
            return False

        index_matricula = matriculas.index(matricula)

        matricula.data_confirmacao = datetime.datetime.now()

        matriculas[index_matricula] = matricula

        return True
        
    
    def cancelar_matricula(self, disciplina):
        if type(matricula) is not Matricula:
            return False
        
        if matricula not in self.matriculas:
            return False

        index_matricula = matriculas.index(matricula)

        matricula.data_cancelamento = datetime.datetime.now()

        matriculas[index_matricula] = matricula

        return True


#NAO MOVER ESSE IMPORT CIRCULAR PARA CIMA
from Disciplina import Disciplina
from Matricula import Matricula