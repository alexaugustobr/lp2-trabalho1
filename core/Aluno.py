from Pessoa import Pessoa
from Usuario import Usuario
class Aluno(Pessoa,Usuario):
    sigla_curso = None
    matriculas = []


#NAO MOVER ESSE IMPORT CIRCULAR PARA CIMA
from Disciplina import Disciplina
from Matricula import Matricula

def disciplinas_aluno(self):
    nome_disciplinas = []
    for matricula in matriculas:
        nome_disciplinas.append(matricula.disciplina.nome)
    
    return nome_disciplinas

def matricular(self, Matricula):
    if type(matricula) is not Matricula:
        return False
    self.matricula = matricula
    return True

    for 

  

def confirmar_matricular(self):

